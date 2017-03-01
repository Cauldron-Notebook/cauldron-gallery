# Conclusions

The above examples should give you a basic idea of how joins work using the
three approaches as well as a feeling for how each approach works in general
(at least for select statements). Pandas is the clear winner for being concise
and Pandas joins are also very fast. The obvious caveat is that the data must
be loaded locally in memory for Pandas to be used, which isn't always the best
approach.

The SQLAlchemy expression language may seem foreign if you haven't been exposed
to it much, but it is very easy to get comfortable with it. Where the
expression language excels is readability because it is Pythonic in its style
and allows you to break complex statements up into readable pieces that can
easily be combined to build a complex query. SQLAlchemy expression syntax also
has the benefit of converting your code into well-optimized SQL, which is most
often better than what someone would write themselves by hand.
