## 1. Spreadsheet Overview
- **Sheet Name**: Opex CTRL
- **Key Sections Identified**:
  - Base - $25mm
  - Growth - $25mm
  - Base - $50mm
  - Base - $50mm (R&D)
  - Other Costs - % YoY Growth

## 2. Detailed Section Analysis

### Base - $25mm
- **Section Type**: Custom Opex Section
- **Description & Purpose**: A base-operating-expenses block representing a $25 million annual opex scenario. Captures labor-related costs and selected non-labor cost buckets as a standalone baseline for planning and comparison against Growth and larger Base scenarios.
- **Cell Range**: B14, B21, B28, B35, B42, B49, B56, B66, B73, B80, B87, B94, B101, B108, B115, B121, B127, B134, B140, B146, B153, B159, B165, B172, B180, B187, B194, B201, B208, B215, B222, B229, B236, B243, B250, B256, B262, B270, B276, B282, B288, B294, B300, B306, B312, B318, B324, B330, B336, B342, B348, B354, B360, B366, B372, B378, B384, B390, B396, B402, B408, B414, B420, B426, B432, B438, B444, B450, B456, B462, B468, B474, B480, B486, B492, B498, B504, B510, B516, B522, B528, B534, B540, B546, B552, B558, B564, B570, B576, B582, B588, B594, B600, B606, B614, B620, B626, B632, B638, B644, B650, B656, B662, B668, B674, B680, B686, B692, B698, B704, B710, B716, B722, B728, B734, B740, B746, B752, B758, B764, B770, B776, B782, B788, B794, B800, B806, B812, B818, B824, B830, B836, B842, B850, B856, B862, B868, B874, B880, B886, B892, B898, B904, B910, B916, B922, B928, B934, B940, B946, B952, B958, B964, B970, B976, B982, B988, B994, B1000, B1006, B1012, B1018, B1024, B1030, B1036, B1042, B1048, B1054, B1060, B1068, B1074, B1080, B1086, B1092, B1098, B1104, B1110, B1116, B1122, B1128, B1134, B1140, B1146, B1152, B1158, B1164, B1170, B1176, B1182, B1188, B1194, B1200, B1206, B1212, B1218, B1224, B1230, B1236, B1242, B1248, B1254, B1260, B1266, B1272, B1278, B1284, B1290, B1296, B1304, B1310, B1316, B1322, B1328, B1334, B1340, B1346, B1352, B1358, B1364, B1370, B1376, B1382, B1388, B1394, B1400, B1406, B1412, B1418, B1424, B1430, B1436, B1442, B1448, B1454, B1460, B1466, B1472, B1478, B1484, B1490, B1496, B1502, B1508, B1514, B1522, B1528, B1534, B1540, B1546, B1552, B1558, B1564, B1570, B1576, B1582, B1588, B1594, B1600, B1606, B1612, B1618, B1624, B1630, B1636, B1642, B1648, B1654, B1660, B1666, B1672, B1678, B1684, B1690, B1696, B1702, B1708, B1714, B1720, B1726, B1732, B1738, B1744, B1750, B1756, B1762, B1768, B1774, B1780, B1786, B1792, B1798, B1804, B1810, B1816, B1822, B1828, B1834, B1840, B1846, B1852, B1858, B1864, B1870, B1876, B1882, B1888, B1894, B1900, B1906, B1912, B1918, B1924, B1930, B1936, B1942, B1948, B1954, B1960, B1966, B1972, B1978, B1984, B1990, B1996, B2002, B2008, B2014, B2020, B2026, B2032, B2038, B2044, B2050, B2056, B2062, B2068, B2074, B2080, B2086, B2092, B2098, B2104, B2110, B2116, B2122, B2128, B2134, B2140, B2146, B2152, B2158, B2164, B2170, B2176, B2182, B2188, B2194, B2200, B2206, B2212, B2218, B2224, B2230, B2236, B2242, B2248, B2254, B2260, B2266, B2272, B2278, B2284, B2290, B2296, B2302, B2308, B2314, B2320, B2326, B2332, B2338, B2344, B2350, B2356, B2362, B2368, B2374, B2380, B2386, B2392, B2398, B2404, B2410, B2416, B2422, B2428, B2434, B2440, B2446, B2452, B2458, B2464, B2470, B2476, B2482, B2488
- **Time Series Horizon**:
  - Dates Location (Year): E6:Q6 → ds_1 (Annual; 2015-01-01 to 2027-01-01)
  - Dates Location (Monthly): T6:FS6 → ds_2 (Monthly; 2015-01-01 to 2027-12-01 pattern)
  - Month Labels: B7 (Month header) and E8:Q8 → ds_3 (Monthly sub-periods)
  - Optional/Additional Axis: I1472:Q1472 → ds_4 (Annual; 2000-01-01 onward for nine periods)
- **Date Range**:
  - ds_1: 2015-01-01 to 2027-01-01
  - ds_2: 2015-01-01 to 2027-12-01 (monthly grid across 12 months per year)
  - ds_3: 2015-01-31 to 2027-12-31 (monthly)
  - ds_4: 2000-01-01 to 2008-01-01 (nine periods)
- **Frequency**:
  - ds_1: Annual
  - ds_2: Monthly (repeating annual cycle)
  - ds_3: Monthly
  - ds_4: Annual (nine periods)
- **Key Components**: Labor costs (wages %), Travel % of Wages, Other Costs (Airplane) % of Wages, Other Facilities Cost % of Rent, Marketing Cost metrics, Non-Salary G&A per Head, Capex-related adjustments, and assorted wage-based vs. non-wage cost buckets.
- **Notes & Customizations**: This is a highly customized base-opex scenario used for planning and comparison across multiple base sizes. It relies on several percent-of-wage and per-head cost drivers, plus numerous non-salary categories, making it a bespoke operating-expenses planning block rather than a standard P&L line-item sheet.

---

### Growth - $25mm
- **Section Type**: Custom Opex Section
- **Description & Purpose**: A growth-oriented opex block representing a $25 million annual increase pathway. This section models how opex would scale under growth assumptions, including wage-based cost drivers and selected non-labor cost buckets.
- **Cell Range**: B15, B22, B29, B36, B43, B50, B57, B67, B74, B81, B88, B95, B102, B109, B116, B122, B128, B135, B141, B147, B154, B160, B166, B173, B181, B188, B195, B202, B209, B216, B223, B230, B237, B244, B251, B257, B263, B271, B277, B283, B289, B295, B301, B307, B313, B319, B325, B331, B337, B343, B349, B355, B361, B367, B373, B379, B385, B391, B397, B403, B409, B415, B421, B427, B433, B439, B445, B451, B457, B463, B469, B475, B481, B487, B493, B499, B505, B511, B517, B523, B529, B535, B541, B547, B553, B559, B565, B571, B577, B583, B589, B595, B601, B607, B615, B621, B627, B633, B639, B645, B651, B657, B663, B669, B675, B681, B687, B693, B699, B705, B711, B717, B723, B729, B735, B741, B747, B753, B759, B765, B771, B777, B783, B789, B795, B801, B807, B813, B819, B825, B831, B837, B843, B851, B857, B863, B869, B875, B881, B887, B893, B899, B905, B911, B917, B923, B929, B935, B941, B947, B953, B959, B965, B971, B977, B983, B989, B995, B1001, B1007, B1013, B1019, B1025, B1031, B1037, B1043, B1049, B1055, B1061, B1069, B1075, B1081, B1087, B1093, B1099, B1105, B1111, B1117, B1123, B1129, B1135, B1141, B1147, B1153, B1159, B1165, B1171, B1177, B1183, B1189, B1195, B1201, B1207, B1213, B1219, B1225, B1231, B1237, B1243, B1249, B1255, B1261, B1267, B1273, B1279, B1285, B1291, B1297, B1305, B1311, B1317, B1323, B1329, B1335, B1341, B1347, B1353, B1359, B1365, B1371, B1377, B1383, B1389, B1395, B1401, B1407, B1413, B1419, B1425, B1431, B1437, B1443, B1449, B1455, B1461, B1467, B1473, B1479, B1485, B1491, B1497, B1503, B1509, B1515, B1523, B1529, B1535, B1541, B1547, B1553, B1559, B1565, B1571, B1577, B1583, B1589, B1595, B1601, B1607, B1613, B1619, B1625, B1631, B1637, B1643, B1649, B1655, B1661, B1667, B1673, B1679, B1685, B1691, B1697, B1703, B1709, B1715, B1721, B1727, B1733, B1739, B1745, B1751, B1757, B1763, B1769, B1775, B1781, B1787, B1793, B1799, B1805, B1811, B1817, B1823, B1829, B1835, B1841, B1847, B1853, B1859, B1865, B1871, B1877, B1883, B1889, B1895, B1901, B1909, B1915, B1921, B1927, B1933, B1939, B1945, B1951, B1957, B1963, B1969, B1975, B1981, B1987, B1993, B1999, B2005, B2011, B2017, B2023, B2029, B2035, B2041, B2047, B2053, B2059, B2065, B2071, B2077, B2083, B2089, B2095, B2101, B2107, B2113, B2119, B2125, B2131, B2137, B2143, B2149, B2155, B2161, B2167, B2173, B2179, B2185, B2191, B2197, B2206, B2212, B2218, B2224, B2230, B2236, B2242, B2248, B2254, B2260, B2266, B2272, B2278, B2284, B2290, B2296, B2302, B2308, B2314, B2320, B2326, B2332, B2338, B2344, B2350, B2356, B2362, B2368, B2374, B2380, B2386, B2392, B2398, B2404, B2410, B2416, B2422, B2428, B2434, B2440, B2446, B2452, B2458, B2464, B2470, B2476, B2482, B2488
- **Time Series Horizon**:
  - Dates Location (Year): E6:Q6 → ds_1 (Annual)
  - Dates Location (Monthly): T6:FS6 → ds_2 (Monthly)
  - Months: B7/Dates header for months; E8:Q8 → ds_3 (Monthly)
  - ds_4 axis (annual, 9 periods) via I1472:Q1472 → ds_4
- **Date Range**:
  - ds_1: 2015-01-01 to 2027-01-01
  - ds_2: 2015-01-01 to 2027-12-01 pattern
  - ds_3: 2015-01-31 to 2027-12-31
  - ds_4: 2000-01-01 to 2008-01-01
- **Frequency**:
  - ds_1: Annual
  - ds_2: Monthly
  - ds_3: Monthly
  - ds_4: Annual
- **Key Components**: Labor costs (wages % of wages), Travel % of Wages, Other Costs (Airplane) % of Wages, Other Costs (Rent/Facilities) % of Rent, Marketing spend efficiency, and multiple Non-Salary G&A and Benefit-related buckets.
- **Notes & Customizations**: Growth-focused block with similar structure to the base, emphasizing scalable or incremental opex drivers; includes percentage-of-wages-based allocations and per-head metrics for planning.

---

### Base - $50mm
- **Section Type**: Custom Opex Section
- **Description & Purpose**: A larger base opex scenario at $50 million annual scale. This block mirrors the Base - $25mm structure but assumes a higher starting point, enabling comparison of efficiency, scale effects, and non-labor cost allocation at a larger operating footprint.
- **Cell Range**: B16, B23, B30, B37, B44, B51, B58, B68, B75, B82, B89, B96, B103, B110, B117, B123, B129, B136, B142, B148, B155, B161, B167, B174, B182, B189, B196, B203, B210, B217, B224, B231, B238, B245, B252, B258, B264, B272, B278, B284, B290, B296, B302, B308, B314, B320, B326, B332, B338, B344, B350, B356, B362, B368, B374, B380, B386, B392, B398, B404, B410, B416, B422, B429, B436, B442, B448, B454, B460, B466, B472, B478, B484, B490, B496, B502, B508, B514, B520, B526, B532, B538, B544, B550, B556, B562, B568, B574, B580, B586, B592, B598, B604, B612, B618, B624, B630, B636, B642, B648, B654, B660, B666, B672, B678, B684, B690, B696, B702, B708, B714, B720, B726, B732, B738, B744, B750, B756, B762, B768, B774, B780, B786, B792, B798, B804, B810, B816, B822, B828, B834, B840, B848, B854, B860, B866, B872, B878, B884, B890, B896, B902, B908, B914, B920, B926, B932, B938, B944, B950, B956, B962, B968, B974, B980, B986, B992, B998, B1004, B1010, B1016, B1022, B1028, B1034, B1040, B1046, B1052, B1058, B1064, B1070, B1076, B1082, B1088, B1094, B1100, B1106, B1112, B1118, B1124, B1130, B1136, B1142, B1148, B1154, B1160, B1166, B1172, B1178, B1184, B1190, B1196, B1202, B1208, B1214, B1220, B1226, B1232, B1238, B1244, B1250, B1256, B1262, B1268, B1274, B1280, B1286, B1292, B1298, B1306, B1312, B1318, B1324, B1330, B1336, B1342, B1348, B1354, B1360, B1366, B1372, B1378, B1384, B1390, B1396, B1402, B1408, B1414, B1420, B1426, B1432, B1438, B1444, B1450, B1456, B1462, B1468, B1474, B1480, B1486, B1492, B1498, B1504, B1510, B1516, B1524, B1530, B1536, B1542, B1548, B1554, B1560, B1566, B1572, B1578, B1584, B1590, B1596, B1602, B1608, B1614, B1620, B1626, B1632, B1638, B1644, B1650, B1656, B1662, B1668, B1674, B1680, B1686, B1692, B1698, B1704, B1710, B1716, B1722, B1728, B1734, B1740, B1746, B1752, B1758, B1764, B1770, B1776, B1782, B1788, B1794, B1800, B1806, B1812, B1818, B1824, B1830, B1836, B1842, B1848, B1854, B1860, B1866, B1872, B1878, B1884, B1891, B1897, B1903, B1911, B1917, B1923, B1929, B1935, B1941, B1947, B1953, B1959, B1965, B1971, B1977, B1983, B1989, B1995, B2001, B2007, B2013, B2019, B2025, B2031, B2037, B2043, B2049, B2055, B2061, B2067, B2073, B2079, B2085, B2091, B2097, B2103, B2109, B2115, B2121, B2127, B2133, B2139, B2145, B2151, B2157, B2163, B2169, B2175, B2181, B2187, B2193, B2199, B2207, B2213, B2219, B2225, B2231, B2237, B2243, B2249, B2255, B2261, B2267, B2273, B2279, B2285, B2291, B2297, B2303, B2309, B2315, B2321, B2327, B2333, B2339, B2345, B2351, B2357, B2363, B2369, B2375, B2381, B2387, B2393, B2399, B2405, B2411, B2417, B2423, B2429, B2435, B2441, B2447, B2453, B2459, B2465, B2471, B2477, B2483, B2489
- **Time Series Horizon**:
  - Dates Location (Year): E6:Q6 → ds_1 (Annual)
  - Dates Location (Monthly): T6:FS6 → ds_2 (Monthly)
  - Months: B7/B8 headers; E8:Q8 → ds_3 (Monthly)
  - ds_4 axis via I1480:Q1480? (if applicable in this Growth block context) → ds_4
- **Date Range**:
  - ds_1: 2015-01-01 to 2027-01-01
  - ds_2: 2015-01-01 to 2027-12-01
  - ds_3: 2015-01-31 to 2027-12-31
  - ds_4: 2000-01-01 to 2008-01-01 (if used)
- **Frequency**:
  - ds_1: Annual
  - ds_2: Monthly
  - ds_3: Monthly
  - ds_4: Annual
- **Key Components**: Wage-based growth drivers, Travel, Other costs (Airplane), Facilities, Marketing, and broad non-salary Opex buckets adjusted for growth.
- **Notes & Customizations**: Represents growth acceleration versus the Base - $25mm scenario; uses similar cost-driver structure to enable direct comparison of scale effects and efficiency.

---

### Base - $50mm
- **Section Type**: Custom Opex Section
- **Description & Purpose**: A larger base opex scenario at $50 million annually. Enables assessment of scale effects, efficiency gains, and non-labor-cost allocation at a higher operating footprint.
- **Cell Range**: B16, B23, B30, B37, B44, B51, B58, B68, B75, B82, B89, B96, B103, B110, B117, B123, B129, B136, B142, B148, B155, B161, B167, B174, B182, B189, B196, B203, B210, B217, B224, B231, B238, B245, B252, B258, B264, B272, B278, B284, B290, B296, B302, B308, B314, B320, B326, B332, B338, B344, B350, B356, B362, B368, B374, B380, B386, B392, B398, B404, B410, B416, B422, B429, B436, B442, B448, B454, B460, B466, B472, B478, B484, B490, B496, B502, B508, B514, B520, B526, B532, B538, B544, B550, B556, B562, B568, B574, B580, B586, B592, B598, B604, B612, B618, B624, B630, B636, B642, B648, B654, B660, B666, B672, B678, B684, B690, B696, B702, B708, B714, B720, B726, B732, B738, B744, B750, B756, B762, B768, B774, B780, B786, B792, B798, B804, B810, B816, B822, B828, B834, B840, B848, B854, B860, B866, B872, B878, B884, B890, B896, B902, B908, B914, B920, B926, B932, B938, B944, B950, B956, B962, B968, B974, B980, B986, B992, B998, B1004, B1010, B1016, B1022, B1028, B1034, B1040, B1046, B1052, B1058, B1064, B1070, B1076, B1082, B1088, B1094, B1100, B1106, B1112, B1118, B1124, B1130, B1136, B1142, B1148, B1154, B1160, B1166, B1172, B1178, B1184, B1190, B1196, B1202, B1208, B1214, B1220, B1226, B1232, B1238, B1244, B1250, B1256, B1262, B1268, B1274, B1280, B1286, B1292, B1298, B1306, B1312, B1318, B1324, B1330, B1336, B1342, B1348, B1354, B1360, B1366, B1372, B1378, B1384, B1390, B1396, B1402, B1408, B1414, B1420, B1426, B1432, B1438, B1444, B1450, B1456, B1462, B1468, B1474, B1480, B1486, B1492, B1498, B1504, B1510, B1516, B1524, B1530, B1536, B1542, B1548, B1554, B1560, B1566, B1572, B1578, B1584, B1590, B1596, B1602, B1608, B1614, B1620, B1626, B1632, B1638, B1644, B1650, B1656, B1662, B1668, B1674, B1680, B1686, B1692, B1698, B1704, B1710, B1716, B1722, B1728, B1734, B1740, B1746, B1752, B1758, B1764, B1770, B1776, B1782, B1788, B1794, B1800, B1806, B1812, B1818, B1824, B1830, B1836, B1842, B1848, B1854, B1860, B1866, B1872, B1878, B1884, B1891, B1897, B1903, B1911, B1917, B1923, B1929, B1935, B1941, B1947, B1953, B1959, B1965, B1971, B1977, B1983, B1989, B1995, B2001, B2007, B2013, B2019, B2025, B2031, B2037, B2043, B2049, B2055, B2061, B2067, B2073, B2079, B2085, B2091, B2097, B2103, B2109, B2115, B2121, B2127, B2133, B2139, B2145, B2151, B2157, B2163, B2169, B2175, B2181, B2187, B2193, B2199, B2207, B2213, B2219, B2225, B2231, B2237, B2243, B2249, B2255, B2261, B2267, B2273, B2279, B2285, B2291, B2297, B2303, B2309, B2315, B2321, B2327, B2333, B2339, B2345, B2351, B2357, B2363, B2369, B2375, B2381, B2387, B2393, B2399, B2405, B2411, B2417, B2423, B2429, B2435, B2441, B2447, B2453, B2459, B2465, B2471, B2477, B2483, B2489
- **Time Series Horizon**:
  - Dates Location (Year): E6:Q6 → ds_1 (Annual)
  - Dates Location (Monthly): T6:FS6 → ds_2 (Monthly)
  - Months: E7?–D8; E8:Q8 → ds_3 (Monthly)
  - ds_4 axis (annual, 9 periods) if applicable
- **Date Range**:
  - ds_1: 2015-01-01 to 2027-01-01
  - ds_2: 2015-01-01 to 2027-12-01
  - ds_3: 2015-01-31 to 2027-12-31
  - ds_4: 2000-01-01 to 2008-01-01
- **Frequency**:
  - ds_1: Annual
  - ds_2: Monthly
  - ds_3: Monthly
  - ds_4: Annual
- **Key Components**: Base labor and non-labor opex buckets at a higher scale; similar structure to the $25mm base with intensified allocations.
- **Notes & Customizations**: This is a high-scale base scenario used to stress-test cost structures and to benchmark against Growth and smaller Base scenarios.

---

### Base - $50mm (R&D)
- **Section Type**: Custom Opex Section
- **Description & Purpose**: A specialized Base - $50mm scenario that includes R&D-linked cost allocations. Enables assessment of R&D-related opex alongside standard base costs, useful for evaluating the impact of R&D spend on overall opex.
- **Cell Range**: B17, B24, B31, B38, B45, B52, B59, B69, B76, B83, B90, B97, B104, B111, B118, B124, B130, B137, B143, B149, B156, B162, B168, B175, B183, B190, B197, B204, B211, B218, B225, B232, B239, B246, B253, B259, B265, B273, B279, B285, B291, B297, B303, B309, B315, B321, B327, B333, B339, B345, B351, B357, B363, B369, B375, B381, B387, B393, B399, B405, B411, B417, B423, B430, B437, B443, B449, B455, B461, B467, B473, B479, B485, B491, B497, B503, B509, B515, B521, B527, B533, B539, B545, B551, B557, B563, B569, B575, B581, B587, B593, B599, B605, B613, B619, B625, B631, B637, B643, B649, B655, B661, B667, B673, B679, B685, B691, B697, B703, B709, B715, B721, B727, B733, B739, B745, B751, B757, B763, B769, B775, B781, B787, B793, B799, B805, B811, B817, B823, B829, B835, B841, B848, B854, B860, B866, B872, B878, B884, B890, B896, B902, B908, B914, B920, B926, B932, B938, B944, B950, B956, B962, B968, B974, B980, B986, B992, B998, B1004, B1010, B1016, B1022, B1028, B1034, B1040, B1046, B1052, B1058, B1064, B1070, B1076, B1082, B1088, B1094, B1100, B1106, B1112, B1118, B1124, B1130, B1136, B1142, B1148, B1154, B1160, B1166, B1172, B1178, B1184, B1190, B1196, B1202, B1208, B1214, B1220, B1226, B1232, B1238, B1244, B1250, B1256, B1262, B1268, B1274, B1280, B1286, B1292, B1298, B1306, B1312, B1318, B1324, B1330, B1336, B1342, B1348, B1354, B1360, B1366, B1372, B1378, B1384, B1390, B1396, B1402, B1408, B1414, B1420, B1426, B1432, B1438, B1444, B1450, B1456, B1462, B1468, B1474, B1480, B1486, B1492, B1498, B1504, B1510, B1516, B1524, B1530, B1536, B1542, B1548, B1554, B1560, B1566, B1572, B1578, B1584, B1590, B1596, B1602, B1608, B1614, B1620, B1626, B1632, B1638, B1644, B1650, B1656, B1662, B1668, B1674, B1680, B1686, B1692, B1698, B1704, B1710, B1716, B1722, B1728, B1734, B1740, B1746, B1752, B1758, B1764, B1770, B1776, B1782, B1788, B1794, B1800, B1806, B1812, B1818, B1824, B1830, B1836, B1842, B1848, B1854, B1860, B1866, B1872, B1878, B1884, B1891, B1897, B1903, B1911, B1917, B1923, B1929, B1935, B1941, B1947, B1953, B1959, B1965, B1971, B1977, B1983, B1989, B1995, B2001, B2007, B2013, B2019, B2025, B2031, B2037, B2043, B2049, B2055, B2061, B2067, B2073, B2079, B2085, B2091, B2097, B2103, B2109, B2115, B2121, B2127, B2133, B2139, B2145, B2151, B2157, B2163, B2169, B2175, B2181, B2187, B2193, B2199, B2207, B2213, B2219, B2225, B2231, B2237, B2243, B2249, B2255, B2261, B2267, B2273, B2279, B2285, B2291, B2297, B2303, B2309, B2315, B2321, B2327, B2333, B2339, B2345, B2351, B2357, B2363, B2369, B2375, B2381, B2387, B2393, B2399, B2405, B2411, B2417, B2423, B2429, B2435, B2441, B2447, B2453, B2459, B2465, B2471, B2477, B2483, B2489
- **Time Series Horizon**:
  - Dates Location (Year): E6:Q6 → ds_1 (Annual)
  - Dates Location (Monthly): T6:FS6 → ds_2 (Monthly)
  - Months/Other Axes: E8:Q8 → ds_3 (Monthly)
  - ds_4 axis (annual, 9 periods)
- **Date Range**:
  - ds_1: 2015-01-01 to 2027-01-01
  - ds_2: 2015-01-01 to 2027-12-01
  - ds_3: 2015-01-31 to 2027-12-31
  - ds_4: 2000-01-01 to 2008-01-01
- **Frequency**:
  - ds_1: Annual
  - ds_2: Monthly
  - ds_3: Monthly
  - ds_4: Annual
- **Key Components**: Higher-scale non-labor opex buckets, R&D-specific cost drivers, and core Base-category allocations at a larger footprint.
- **Notes & Customizations**: This block purposefully escalates the base footprint by including R&D-linked expense lines, enabling scenario comparison with the other base and growth blocks.

---

### Base - $50mm (R&D)
- **Section Type**: Custom Opex Section
- **Description & Purpose**: A dedicated Base - $50mm (R&D) scenario focusing on R&D-related opex allocations within a larger base footprint. Useful for evaluating how R&D spend interacts with overall operating expenses at scale.
- **Cell Range**: B17, B24, B31, B38, B45, B52, B59, B69, B76, B83, B90, B97, B104, B111, B118, B124, B130, B137, B143, B149, B156, B162, B168, B175, B183, B190, B197, B204, B211, B218, B225, B232, B239, B246, B253, B259, B265, B273, B279, B285, B291, B297, B303, B309, B315, B321, B327, B333, B339, B345, B351, B357, B363, B369, B375, B381, B387, B393, B399, B405, B411, B417, B423, B430, B437, B443, B449, B455, B461, B467, B473, B479, B485, B491, B497, B503, B509, B515, B521, B527, B533, B539, B545, B551, B557, B563, B569, B575, B581, B587, B593, B599, B605, B613, B619, B625, B631, B637, B643, B649, B655, B661, B667, B673, B679, B685, B691, B697, B703, B709, B715, B721, B727, B733, B739, B745, B751, B757, B763, B769, B775, B781, B787, B793, B799, B805, B811, B817, B823, B829, B835, B841, B848, B854, B860, B866, B872, B878, B884, B890, B896, B902, B908, B914, B920, B926, B932, B938, B944, B950, B956, B962, B968, B974, B980, B986, B992, B998, B1004, B1010, B1016, B1022, B1028, B1034, B1040, B1046, B1052, B1058, B1064, B1070, B1076, B1082, B1088, B1094, B1100, B1106, B1112, B1118, B1124, B1130, B1136, B1142, B1148, B1154, B1160, B1166, B1172, B1178, B1184, B1190, B1196, B1202, B1208, B1214, B1220, B1226, B1232, B1238, B1244, B1250, B1256, B1262, B1268, B1274, B1280, B1286, B1292, B1298, B1306, B1312, B1318, B1324, B1330, B1336, B1342, B1348, B1354, B1360, B1366, B1372, B1378, B1384, B1390, B1396, B1402, B1408, B1414, B1420, B1426, B1432, B1438, B1444, B1450, B1456, B1462, B1468, B1474, B1480, B1486, B1492, B1498, B1504, B1510, B1516, B1524, B1530, B1536, B1542, B1548, B1554, B1560, B1566, B1572, B1578, B1584, B1590, B1596, B1602, B1608, B1614, B1620, B1626, B1632, B1638, B1644, B1650, B1656, B1662, B1668, B1674, B1680, B1686, B1692, B1698, B1704, B1710, B1716, B1722, B1728, B1734, B1740, B1746, B1752, B1758, B1764, B1770, B1776, B1782, B1788, B1794, B1800, B1806, B1812, B1818, B1824, B1830, B1836, B1842, B1848, B1854, B1860, B1866, B1872, B1878, B1884, B1891, B1897, B1903, B1911, B1917, B1923, B1929, B1935, B1941, B1947, B1953, B1959, B1965, B1971, B1977, B1983, B1989, B1995, B2001, B2007, B2013, B2019, B2025, B2031, B2037, B2043, B2049, B2055, B2061, B2067, B2073, B2079, B2085, B2091, B2097, B2103, B2109, B2115, B2121, B2127, B2133, B2139, B2145, B2151, B2157, B2163, B2169, B2175, B2181, B2187, B2193, B2199, B2207, B2213, B2219, B2225, B2231, B2237, B2243, B2249, B2255, B2261, B2267, B2273, B2279, B2285, B2291, B2297, B2303, B2309, B2315, B2321, B2327, B2333, B2339, B2345, B2351, B2357, B2363, B2369, B2375, B2381, B2387, B2393, B2399, B2405, B2411, B2417, B2423, B2429, B2435, B2441, B2447, B2453, B2459, B2465, B2471, B2477, B2483, B2489
- **Time Series Horizon**:
  - Dates Location (Year): ds_1 at E6:Q6; ds_2 at T6:FS6; ds_3 at E8:Q8; ds_4 if applicable
- **Date Range**:
  - ds_1: 2015-01-01 to 2027-01-01
  - ds_2: 2015-01-01 to 2027-12-01
  - ds_3: 2015-01-31 to 2027-12-31
  - ds_4: 2000-01-01 to 2008-01-01
- **Frequency**:
  - ds_1: Annual
  - ds_2: Monthly
  - ds_3: Monthly
  - ds_4: Annual
- **Key Components**: R&D-cost related allocations within the larger base framework; Core Base opex buckets with added R&D emphasis.
- **Notes & Customizations**: Specialization for R&D cost flow within a $50mm base; used to compare against non-R&D/Base blocks.

---

### Base - $50mm (R&D) – Additional Notes
- **Section Type**: Custom Opex Section
- **Description & Purpose**: Additional R&D-focused base block to isolate the impact of R&D spend on operating expenses, enabling targeted sensitivity analysis.
- **Cell Range**: Non-contiguous (mirrors the Base - $50mm ranges with an R&D emphasis)
- (Note: The exact contiguous cell-range representation is non-trivial due to the non-contiguous nature of the inverted_index ranges; see the Base - $50mm section for the comprehensive list of involved B-range labels.)

- **Time Series Horizon**:
  - ds_1/ds_2/ds_3: as above for the Base - $50mm context
- **Date Range**:
  - As above for the Base - $50mm block
- **Frequency**:
  - As above for the Base - $50mm block
- **Key Components**: Explicit inclusion of R&D-linked costs alongside standard base opex allocations.
- **Notes & Customizations**: This entry highlights the dedicated R&D cost stream within the larger $50mm base framework.

---

### Other Costs - % YoY Growth
- **Section Type**: Key Metrics Table
- **Description & Purpose**: A high-level driver metric section capturing YoY growth for other costs as a percentage of wages. Serves as a monitoring/control metric rather than a line-item spend forecast.
- **Cell Range**: B63, B65
- **Time Series Horizon**:
  - Dates Location: N/A (not a primary time-series container)
  - Date Range: N/A
  - Frequency: N/A
- **Date/Time Context**: Not a primary time-series block; used to drive YoY growth assumptions elsewhere.
- **Key Components**: YoY growth values and related delta indicators for other costs.
- **Notes & Customizations**: This is a meta-cost-growth metric rather than a direct expense forecast; used to adjust or validate other sections’ growth rates.