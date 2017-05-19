# HathiTrust Usage Analysis

As part of some work to expand the [SimplyE
project](http://www.librarysimplified.org/) to include more materials
useful to the research community, I've done some basic analysis of
[HathiTrust](https://www.hathitrust.org/about)
usage.

HathiTrust describes itself as: 

    a partnership of major research institutions and libraries working to ensure that the cultural record is preserved and accessible long into the future. The mission of HathiTrust is to contribute to research, scholarship, and the common good by collaboratively collecting, organizing, preserving, communicating, and sharing the record of human knowledge. There are more than 120 partners in HathiTrust, and membership is open to institutions worldwide.

It contains more than 15 million volumes, including 5.8 million open volumes in the
public domain. NYPL, through its Google Library Project partnership, has
contributed more than 300,000 volumes to HathiTrust. For more info see the
[HathiTrust about page](https://www.hathitrust.org/about).

The data below covers the period May 8, 2014 - May 7, 2017.



## Headline numbers

**15,095,384** retrievable records from the Hathifiles
(Pandas choked on a small subset of records which are not included here, and are
almost certainly not among the most-viewed items)

**3,247,601** distinct HathiTrust volume IDs
(that I was able to scrape out of three years of analytics data)

### Most viewed titles

**See [top_open_items.txt](txt/top_open_items.txt) for the full list**

| Title |  Uses | Publication Date|
|-------|-------|-----------------|
| <a href="https://babel.hathitrust.org/cgi/pt?id=mdp.39015054061430">Quicksand,</a> | 823739 views | 1928 |
| <a href="https://babel.hathitrust.org/cgi/pt?id=mdp.39015011274175">The surnames of Scotland, their origin meaning and history /</a> | 619250 views | 1962 |
| <a href="https://babel.hathitrust.org/cgi/pt?id=mdp.39015064340733">Solid mensuration,</a> | 452809 views | 1934 |
| <a href="https://babel.hathitrust.org/cgi/pt?id=pst.000057937434">The human figure /</a> | 348795 views | 1907 |
| <a href="https://babel.hathitrust.org/cgi/pt?id=mdp.39015000566789">America is in the heart, a personal history,</a> | 326990 views | 1946 |
| <a href="https://babel.hathitrust.org/cgi/pt?id=mdp.39015004111095">Godey's magazine.</a> | 311573 views | 1850 |
| <a href="https://babel.hathitrust.org/cgi/pt?id=wu.89059402255">Roster of the Confederate soldiers of Georgia, 1861-1865 /</a> | 285162 views | 9999 |



### Most viewed NYPL titles

**See [NYPL_top_open_items.txt](txt/NYPL_top_open_items.txt) for the full list**

|Title |  Uses | Publication Date|
|------|-------|-----------------|
| <a href="https://babel.hathitrust.org/cgi/pt?id=nyp.33433076064025">Miranda /</a> | 48465 views | 1915|
| <a href="https://babel.hathitrust.org/cgi/pt?id=nyp.33433082137914">Wife no. 19, or the story of a life in bondage : being a complete exposé of Mormonism, and revealing the sorrows, sacrifices and sufferings of women in polygamy /</a> | 36158 views | 1875|
|<a href="https://babel.hathitrust.org/cgi/pt?id=nyp.33433067286868">Men of West Virginia ...</a> | 30308 views | 1903|
|<a href="https://babel.hathitrust.org/cgi/pt?id=nyp.33433069455859">Illustrated trade catalogue and price list : manufacturers, importers and jobbers of watchmakers', jewelers' and engravers' supplies of every description : optical goods, chains, charms, etc. : originators of the box matetial [sic] and makers of Swartchild's celebrated watchmakers' benches : 1897-1898 /</a> | 28594 views | 1897|
|<a href="https://babel.hathitrust.org/cgi/pt?id=nyp.33433081844692">A standard history of Stark County, Ohio : an authentic narrative of the past, with particular attention to the modern era in the commercial, industrial, civic and social development : a chronicle of the people, with family lineage and memoirs /</a> | 26722 views | 1916|


### Closed ("Limited View") titles with most attempted views

**See [top_closed_items.txt](txt/top_closed_items.txt) for the full list**

|Title |  Attempted Uses | Publication Date|
|------|-----------------|-----------------|
|<a href="https://babel.hathitrust.org/cgi/pt?id=uc1.b4906221"> The competent manager : a model for effective performance /</a> | 12226 views | 1982|
|<a href="https://babel.hathitrust.org/cgi/pt?id=mdp.39015010576356"> Objects of daily use, with over 1800 figures from University college, London,</a> | 12150 views | 1927|
|<a href="https://babel.hathitrust.org/cgi/pt?id=mdp.39015014559135"> My experiences in the world war,</a> | 10976 views | 1931|
|<a href="https://babel.hathitrust.org/cgi/pt?id=mdp.39015010574575"> Catalogue of Alexandrian coins,</a> | 9132 views | 1933|
|<a href="https://babel.hathitrust.org/cgi/pt?id=uc1.b4522148"> The regimental history of the 3rd Queen Alexandra's own Gurkha rifles from April 1815 to December 1927,</a> | 9088 views | 1929|


## Publication Date analysis

**See [full chart](histogram.html) for better view**

This chart describes the frequency of publication year for the top 500,000 requested items in HathiTrust from
May 2014 - May 2017.

<iframe width="900" height="800" frameborder="0" scrolling="no" src="https://plot.ly/~hadro/12.embed"></iframe>

Note: the embedded histogram on this page only includes the top 40,000 data points
because the free version of plotly has a 40K data point limit; for a full-screen
interactive version of this chart with 500,000 data points, see the **full
[Histogram](histogram.html)**.

Meanwhile, you can toggle the data series on this chart, for example if you want to
view just the items among the top 500K that were requested but could not be
viewed because they are "limited view" items (i.e. closed for copyright reasons).

Notes:
- There are 18,455 volumes not displayed on the [complete chart](histogram.html),
  because they did not fall within the 1600-2020 publication date range
    - 10,349 volumes with a publication date either before 1600 or after 2020
        - 7,770 of those have publication dates of "9999", which almost always
          means they are part of an ongoing publication or serial
    - 8,106 volumes with no valid publication date value in the HathiFiles


## Usage analysis

**See [full chart](usage_log.html) for better view**

This chart describes the usage curve for the top 10,000 items in HathiTrust from
May 2014 - May 2017.

<iframe width="900" height="800" frameborder="0" scrolling="no" src="https://plot.ly/~hadro/11.embed"></iframe>

(For full-screen interactive version of this chart, see [Line Chart](usage_log.html) (or the
[linear scale](usage.html) version as well).

## Tools and method

My steps and the tools I used were very roughly as follows:
- Scraped three years of daily complete Google Analytics urls, using Corey Harper's
  helpful [PygAnalytics tool](https://github.com/chrpr/pyganalytics)
- Downloaded the complete [HathiFiles](https://www.hathitrust.org/hathifiles)
  for May 2017, which includes basic bibliographic and rights metadata for every
      volume in HathiTrust
- Various slicing, dicing, matching, joining, and other manipulations using the
  invaluable [Pandas Python Data Analysis
  Library](http://pandas.pydata.org/)
    - Unholy amounts of regular expressions, via the Pandas `.extract()` and
      `.extractall()` methods
- Ingest of ~15 million rows of HathiFiles into Postgres database, using
  the Pandas `.to_sql()` method
- Data visualization using the [Plotly Python Library](https://plot.ly/python/)
  (including the handy ability to [run Plotly in 'offline
  mode'](https://www.reddit.com/r/IPython/comments/3tibc8/tip_on_how_to_run_plotly_examples_in_offline_mode/),
  so you don't have to constantly upload each iteration of a revised chart).
