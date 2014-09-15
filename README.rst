 "There are official searchers, the "inquisitors"...once in a while, they take up
 the nearest book and leaf through it, searching for disgraceful or dishonorable
 words."

wrongpass
=========
Because you cannot leave your users to choose the wrong pass::

  >>> from wrongpass import I_can_has
  >>> print I_can_has("theboss")
  False
  >>> print I_can_has("1234")
  False
  >>> print I_can_has("cheeseburguer")
  True
  >>> print I_can_has("correct horse battery staple")
  True

Limitations
-----------

Right now this is only an experiment with bloom filters, containing the
list of the 10k Top Passwords `published by Mark Burnett <https://xato.net/passwords/more-top-worst-passwords/>`_.

Of course you can trust the falsation (*), but please, please, do not take the
positives too seriously.

(*) With 0.999 confidence

