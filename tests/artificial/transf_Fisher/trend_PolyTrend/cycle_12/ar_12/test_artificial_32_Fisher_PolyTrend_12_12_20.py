import pyaf.Bench.TS_datasets as tsds
import pyaf.tests.artificial.process_artificial_dataset as art




art.process_dataset(N = 32 , FREQ = 'D', seed = 0, trendtype = "PolyTrend", cycle_length = 12, transform = "Fisher", sigma = 0.0, exog_count = 20, ar_order = 12);