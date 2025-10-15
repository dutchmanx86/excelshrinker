# Future Compression Improvements to Test

## Overview

This document tracks compression techniques that have been **deferred for future testing** due to concerns about LLM interpretation and readability. Since our compressed JSON will be consumed by LLMs, we need to test whether these optimizations help or hurt LLM understanding of the data.

**Last Updated:** 2025-10-13

---

## Deferred Techniques

### 1. Schema-Based Type Encoding

**Status:** 🔬 NEEDS LLM INTERPRETATION TESTING

**Expected Savings:** 15-20% on format_ranges
**Complexity:** Low
**Lossless:** Yes

**Why Deferred:**
We need to test whether LLMs can interpret abbreviated schemas as effectively as full JSON schemas. The compression saves space but may reduce semantic clarity.

**Description:**
Replace verbose JSON keys with short codes and map type values to integers:

```json
// Current (verbose, clear)
{
  "range": "E8:Q8",
  "type": "number",
  "scale": 1000,
  "format_code": "#,##0.00"
}

// Compressed (compact, potentially less clear)
{
  "r": "E8:Q8",
  "t": 0,
  "s": 1,
  "fc": "#,##0.00"
}

// With type mapping
{
  "type_map": {"0": "number", "1": "string", "2": "date", ...},
  "scale_map": {"1": 1000, "2": 1000000},
  "format_ranges": [...]
}
```

**Testing Plan:**

1. **Create Test Datasets:**
   - Convert 10 sample files to both formats (verbose vs encoded)
   - Ensure identical semantic content

2. **LLM Interpretation Tests:**
   - Task: "What is the total revenue in Q1 2023?"
   - Task: "Identify all cells with currency formatting"
   - Task: "Find the range containing employee headcount data"
   - Task: "Summarize the structure of this sheet"

3. **Metrics to Measure:**
   - Accuracy of LLM responses (correct vs incorrect)
   - Response time (tokens processed)
   - Token usage (cost)
   - Confidence scores (if available)

4. **Models to Test:**
   - GPT-4
   - GPT-3.5-turbo
   - Claude 3 (Opus, Sonnet)
   - Gemini Pro

5. **Success Criteria:**
   - Accuracy must be ≥95% of verbose format
   - Token savings must be significant (>20%)
   - No increase in hallucinations or misinterpretations

**Implementation Files (if approved):**
- `compression/schema_encoder.py` (new)
- `compression/format_detector/format_result.py` (add `to_dict_compressed()`)
- `compression/format_compression.py` (add encoding option)

---

### 2. Format Attribute Grouping

**Status:** 🔬 NEEDS LLM INTERPRETATION TESTING

**Expected Savings:** 10-15%
**Complexity:** Medium
**Lossless:** Yes

**Why Deferred:**
Format profiles add a level of indirection that may make it harder for LLMs to understand the data structure at a glance.

**Description:**
Create named format profiles for commonly repeated attribute combinations:

```json
// Current (explicit)
{
  "range": "E8:Q8",
  "type": "number",
  "scale": 1000,
  "format_code": "#,##0"
}

// Compressed (with profile reference)
{
  "range": "E8:Q8",
  "fmt": "num_k"
}

// Profile definition
{
  "format_profiles": {
    "num_k": {"type": "number", "scale": 1000, "format_code": "#,##0"},
    "num_m": {"type": "number", "scale": 1000000, "format_code": "#,##0"},
    "curr_usd": {"type": "currency", "format_code": "$#,##0.00"}
  },
  "format_ranges": [...]
}
```

**Testing Plan:**

1. **Profile Usability Test:**
   - Are profile names intuitive? (num_k = thousands, num_m = millions)
   - Can LLMs resolve profile references correctly?
   - Does the profile dictionary help or hurt comprehension?

2. **LLM Tasks:**
   - "List all ranges with thousands scaling"
   - "What format is applied to range E8:Q8?"
   - "Compare formatting between revenue and expense sections"

3. **Alternative Approaches to Test:**
   - Descriptive profile names: `"thousands_scaled"` vs `"num_k"`
   - Inline expansion vs profile reference
   - Hybrid: expand first occurrence, reference subsequent

4. **Success Criteria:**
   - LLM can accurately resolve profile references
   - No confusion about format attributes
   - Space savings justify the indirection

**Implementation Files (if approved):**
- `compression/format_profiles.py` (new)
- `compression/format_detector/format_result.py` (support profiles)

---

### 3. Binary Compression (gzip/brotli/zstd)

**Status:** ❌ NOT COMPATIBLE WITH LLM CONSUMPTION

**Expected Savings:** 60-80% additional
**Why Deferred:**
JSON must remain as plain text for LLM consumption. Binary compression would require decompression before sending to LLM, which defeats the purpose if the LLM is the primary consumer.

**Possible Future Use Case:**
- If files need to be stored/transmitted and then decompressed before LLM use
- If we implement a service that decompresses on-demand
- If LLMs gain native support for compressed formats (unlikely)

**Not recommended for current workflow.**

---

### 4. Numeric Cell Coordinates

**Status:** ⏸️ LOW PRIORITY

**Expected Savings:** 5-10%
**Why Deferred:**
Excel A1 notation is more human/LLM-readable than numeric coordinates. The space savings are minimal and don't justify the reduced clarity.

```json
// Current (clear)
{"range": "E8:Q10"}

// Numeric (less clear)
{"range": [[4, 7], [16, 9]]}
```

**Decision:** Not pursuing unless other optimizations prove insufficient.

---

### 5. Run-Length Encoding for Scale Patterns

**Status:** ⏸️ COVERED BY RECTANGULAR REGIONS

**Expected Savings:** 20-30%
**Why Deferred:**
Rectangular region detection (already implemented) covers most of this use case. RLE would add complexity for marginal additional gains.

**Decision:** Re-evaluate only if rectangular regions prove insufficient.

---

## Testing Framework

### Setup

Create test harness for LLM interpretation testing:

```python
# test_llm_interpretation.py

import json
from pathlib import Path

class LLMCompressionTester:
    """Test how well LLMs interpret compressed vs verbose JSON."""

    def __init__(self, model_name: str):
        self.model = model_name
        self.test_cases = []

    def add_test_case(self, task: str, expected_answer: str, file_verbose: str, file_compressed: str):
        """Add a test case comparing formats."""
        self.test_cases.append({
            'task': task,
            'expected': expected_answer,
            'verbose_file': file_verbose,
            'compressed_file': file_compressed
        })

    def run_tests(self) -> dict:
        """Run all test cases and return results."""
        results = {
            'verbose': [],
            'compressed': []
        }

        for test in self.test_cases:
            # Test verbose format
            verbose_result = self._query_llm(test['task'], test['verbose_file'])
            results['verbose'].append({
                'task': test['task'],
                'response': verbose_result,
                'correct': self._check_answer(verbose_result, test['expected']),
                'tokens': verbose_result.get('tokens_used', 0)
            })

            # Test compressed format
            compressed_result = self._query_llm(test['task'], test['compressed_file'])
            results['compressed'].append({
                'task': test['task'],
                'response': compressed_result,
                'correct': self._check_answer(compressed_result, test['expected']),
                'tokens': compressed_result.get('tokens_used', 0)
            })

        return self._analyze_results(results)

    def _query_llm(self, task: str, file_path: str) -> dict:
        """Query LLM with task and JSON file."""
        # Implementation depends on LLM API
        pass

    def _check_answer(self, response: dict, expected: str) -> bool:
        """Check if LLM response matches expected answer."""
        # Implementation depends on task type
        pass

    def _analyze_results(self, results: dict) -> dict:
        """Analyze and compare results."""
        verbose_accuracy = sum(r['correct'] for r in results['verbose']) / len(results['verbose'])
        compressed_accuracy = sum(r['correct'] for r in results['compressed']) / len(results['compressed'])

        verbose_tokens = sum(r['tokens'] for r in results['verbose'])
        compressed_tokens = sum(r['tokens'] for r in results['compressed'])

        return {
            'verbose': {
                'accuracy': verbose_accuracy,
                'total_tokens': verbose_tokens,
                'avg_tokens_per_task': verbose_tokens / len(results['verbose'])
            },
            'compressed': {
                'accuracy': compressed_accuracy,
                'total_tokens': compressed_tokens,
                'avg_tokens_per_task': compressed_tokens / len(results['compressed'])
            },
            'comparison': {
                'accuracy_delta': compressed_accuracy - verbose_accuracy,
                'token_savings': (verbose_tokens - compressed_tokens) / verbose_tokens,
                'recommendation': 'use_compressed' if compressed_accuracy >= 0.95 * verbose_accuracy and compressed_tokens < verbose_tokens else 'use_verbose'
            }
        }
```

### Test Cases Template

```python
# Example test cases
tester = LLMCompressionTester(model='gpt-4')

tester.add_test_case(
    task="What is the total revenue for January 2023?",
    expected_answer="$1,234,567",
    file_verbose="samples/income_statement_verbose.json",
    file_compressed="samples/income_statement_compressed.json"
)

tester.add_test_case(
    task="List all cells that contain currency values scaled by 1000.",
    expected_answer="E8:Q10, E15:Q20, ...",
    file_verbose="samples/income_statement_verbose.json",
    file_compressed="samples/income_statement_compressed.json"
)

results = tester.run_tests()
print(json.dumps(results, indent=2))
```

---

## Decision Criteria

Before approving any deferred technique for implementation, it must meet these criteria:

### 1. LLM Interpretation Quality
- ✅ Accuracy ≥ 95% of verbose format
- ✅ No increase in hallucinations
- ✅ No increase in clarification questions needed

### 2. Space Savings
- ✅ Minimum 10% additional compression
- ✅ Savings must justify complexity

### 3. Token Efficiency
- ✅ Reduced token count for LLM processing
- ✅ Cost savings justify implementation effort

### 4. Maintainability
- ✅ Code remains readable and testable
- ✅ Debugging remains feasible
- ✅ Documentation is clear

### 5. Reversibility
- ✅ Can be disabled with feature flag
- ✅ Backward compatibility maintained
- ✅ Migration path exists

---

## Approval Process

1. **Preliminary Testing:** Run LLM interpretation tests on small sample
2. **Review Results:** Analyze accuracy, tokens, and costs
3. **Team Discussion:** Review findings and decide if further testing warranted
4. **Extended Testing:** If promising, test on full dataset with multiple models
5. **Final Decision:** Approve for implementation or close as "not beneficial"
6. **Implementation:** Move to main improvements plan and implement
7. **Monitoring:** Track real-world performance after deployment

---

## Notes

- Keep this document updated as we test and learn
- Document all test results in `compression/test_results/` directory
- Consider A/B testing in production to validate findings
- Re-test periodically as LLM capabilities evolve

---

**Next Steps:**

1. ⏳ Wait until core improvements (rectangular regions, date series dedup, inverted index ranges) are complete
2. ⏳ Implement LLM testing framework
3. ⏳ Run initial tests on schema-based encoding
4. ⏳ Make data-driven decisions based on results

---

**Document Version:** 1.0
**Created:** 2025-10-13
**Status:** Active - Awaiting Core Improvements
