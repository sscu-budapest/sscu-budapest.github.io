---
last_published: 2022.4.26.1
last_version: '0.1'
name: mobility
readme: "<h1>ANET Mobility project</h1>\n<h2>Reports so far</h2>\n<h2>To play around\
  \ with the data</h2>\n<h3>1. fork and clone the repo</h3>\n<p><code>git clone https://github.com/sscu-budapest/mobility</code>\n\
  (preferably fork it first)</p>\n<h3>2. install deps</h3>\n<p><code>pip install -r\
  \ requirements.txt</code></p>\n<h3>3. get the sample data</h3>\n<p>if you are using\
  \ the anet server: \n<code>dvc pull</code></p>\n<p>otherwise, set up the anet server\
  \ to be <code>anetcloud</code> in ssh config and then\n<code>dvc pull --remote anetcloud-ssh</code></p>\n\
  <h3>4. load some samples and look around</h3>\n<p>```python\nfrom src.data_dumps\
  \ import ParsedCols\nfrom src.load_samples import covid_tuesday</p>\n<p>def total_range(s):\n\
  \    return s.max() - s.min()</p>\n<p>samp_df = covid_tuesday.get_full_df()</p>\n\
  <p>samp_df.groupby(ParsedCols.user).agg(\n    {\n        ParsedCols.lon: [\"std\"\
  , total_range],\n        ParsedCols.lat: [\"std\", total_range],\n        ParsedCols.dtime:\
  \ [\"min\", \"max\", \"count\"],\n    }\n).agg([\"mean\", \"median\"]).T\n```</p>\n\
  <table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align:\
  \ right;\">\n      <th></th>\n      <th></th>\n      <th>mean</th>\n      <th>median</th>\n\
  \    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th rowspan=\"2\" valign=\"top\"\
  >lon</th>\n      <th>std</th>\n      <td>0.033919</td>\n      <td>0.001588</td>\n\
  \    </tr>\n    <tr>\n      <th>total_range</th>\n      <td>0.080638</td>\n    \
  \  <td>0.000471</td>\n    </tr>\n    <tr>\n      <th rowspan=\"2\" valign=\"top\"\
  >lat</th>\n      <th>std</th>\n      <td>0.01889</td>\n      <td>0.001067</td>\n\
  \    </tr>\n    <tr>\n      <th>total_range</th>\n      <td>0.045475</td>\n    \
  \  <td>0.000336</td>\n    </tr>\n    <tr>\n      <th rowspan=\"3\" valign=\"top\"\
  >dtime</th>\n      <th>min</th>\n      <td>2020-11-03 07:38:23.900066048</td>\n\
  \      <td>2020-11-03 06:33:42</td>\n    </tr>\n    <tr>\n      <th>max</th>\n \
  \     <td>2020-11-03 18:43:00.657093888</td>\n      <td>2020-11-03 21:08:10</td>\n\
  \    </tr>\n    <tr>\n      <th>count</th>\n      <td>87.307432</td>\n      <td>21.0</td>\n\
  \    </tr>\n  </tbody>\n</table>\n\n<h3>+ if you want to run something that can\
  \ run on the full data set, I suggest using dask</h3>\n<p>```python\nfrom src.data_dumps\
  \ import ParsedCols\nfrom src.load_samples import covid_tuesday\nimport matplotlib.pyplot\
  \ as plt</p>\n<p>samp_ddf = covid_tuesday.get_full_ddf()</p>\n<p>ddf_aggs = (\n\
  \    samp_ddf.assign(hour=lambda df: df[ParsedCols.dtime].dt.hour)\n    .groupby(\"\
  hour\")\n    .agg({ParsedCols.lon: [\"std\"], ParsedCols.lat: \"std\", \"dtime\"\
  : \"count\"})\n    .compute()\n)</p>\n<p>fig, ax1 = plt.subplots()</p>\n<p>ddf_aggs.iloc[:,\
  \ :2].plot(figsize=(14, 7), ax=ax1, xlabel=\"hour in the day\").legend(\n    loc=\"\
  center left\"\n)\nddf_aggs.loc[:, \"dtime\"].plot(figsize=(14, 7), ax=ax1.twinx(),\
  \ color=\"green\").legend(\n    loc=\"center right\"\n)\n```\n<img alt=\"fig1\"\
  \ src=\"report-eg.png\" /></p>\n<h3>load a full week of data</h3>\n<p>```python\n\
  from src.create_samples import covid_sample, non_covid_sample</p>\n<h1>this is about\
  \ 3GB of memory, use get_full_ddf for lazy dask dataframe</h1>\n<p>cov_df = covid_sample.get_full_df()\n\
  ```</p>\n<h2>TODO</h2>\n<ul>\n<li>\"reliable user\" counts</li>\n<li>number of pings</li>\n\
  <li>\"do we know where they live\"</li>\n<li>every month at least once a week</li>\n\
  <li>30 / day (?)</li>\n<li>\n<p>3 in teh morning, 3 in teh evening</p>\n</li>\n\
  <li>\n<p>dump by month</p>\n</li>\n<li>dump by user</li>\n</ul>"
repo_name: mobility
---