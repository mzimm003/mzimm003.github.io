.. _chess-bot:

Chess Bot
============
.. raw:: html

    <p>
    <iframe src="https://ghbtns.com/github-btn.html?user=mzimm003&repo=Chess&type=watch&count=true&size=large&v=2"
    allowtransparency="true" frameborder="0" scrolling="0" width="200px" height="35px"></iframe>
    </p>

Play A Bot
------------
Select a bot to play. Learn more about their construction below.

*Under Construction*

Data Engineering
------------------
The goal of the database supporting our chess bot is to have a large number of 
examples from strong players. Further, it is important that the data is
easily understood by a machine. Then it is adequate to obtain millions of
chess board positions reached by high Elo players where the outcome of the game
is known. The board positions can then effectively be represented as a series of
yes of no statements, mostly regarding each piece and its position within the 8x8
chess board.

Data Gathering
^^^^^^^^^^^^^^^
To achieve so many board positions from high Elo players,
`Computer Chess Rating Lists <http://computerchess.org.uk/ccrl/404/index.html>`_
records millions of games from top chess engines in Portable Game Notation (PGN)
format. These are freely available for download in a compressed format.

Data Preprocessing
^^^^^^^^^^^^^^^^^^^^^^^^
Getting the board positions necessary requires recreating the games played per 
the PGN files. `PettingZoo <https://github.com/Farama-Foundation/PettingZoo>`_,
provided by Farama Foundation, includes a chess environment. This environment
provides observations of the state of the chess board. The specifics can be
found `here <https://pettingzoo.farama.org/environments/classic/chess/>`_. In
short, the observation is a set of board representations, also referred to as 
channels. Each representation is an 8x8 matrix of zeros and ones,
'no's and 'yes's, with respect to a specific piece of information, like
"are there white pawns in this position". There are a few pieces of information
worth clarifying from the PettingZoo documentation so I will include the
channel specifications here:

.. dropdown:: PettingZoo Chess Observation Channels

    +-----------+-------------------------------------+---------------------------------------------------------+
    | Channel   | Information                         |  Specification                                          |
    +===========+=====================================+=========================================================+
    |  0        | Can white castle queenside?         | Non-positional, all ones or all zeros                   |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  1        | Can white castle kingside?          | Non-positional, all ones or all zeros                   |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  2        | Can black castle queenside?         | Non-positional, all ones or all zeros                   |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  3        | Can black castle kingside?          | Non-positional, all ones or all zeros                   |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  4        | Is white or black observing?        | Non-positional, all ones(black) or all zeros(white)     |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  5        | 50 move rule count.                 | One in position of 8x8 matrix flattened to 1 dimension  |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  6        | All ones.                           |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  7        | Where are the observer's pawns?     |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  8        | Where are the observer's knights?   |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  9        | Where are the observer's bishops?   |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  10       | Where are the observer's rooks?     |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  11       | Where are the observer's queens?    |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  12       | Where is the observer's king?       |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  13       | Where are the opponent's pawns?     |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  14       | Where are the opponent's knights?   |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  15       | Where are the opponent's bishops?   |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  16       | Where are the opponent's rooks?     |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  17       | Where are the opponent's queens?    |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  18       | Where is the opponent's king?       |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  19       | Has this position been seen before? | Non-positional, all ones or all zeros                   |
    +-----------+-------------------------------------+---------------------------------------------------------+
    |  20-110   | Repeats of 7-19 for the 7 most      | From most recent to least.                              |
    |           | recent positions.                   |                                                         |
    +-----------+-------------------------------------+---------------------------------------------------------+

To create the database then is a matter of submitting the moves described in the
PGN file to the environment, saving observations with appropriate labels all the
while.

.. image:: /_static/dataProcessing.png
    :scale: 35%
    :align: center

Further, the database is refined to concentrate on more relevant datapoints. On 
advice provided by the `DeepChess <https://arxiv.org/abs/1711.09667>`_ paper,
this includes avoiding positions very early in the game (first 5 moves),
positions immediately after the capture of a piece, and games which ended in a
draw.

The Stats
^^^^^^^^^^^^
+-----------------------------+-------------------------------------+
| Measure                     | Value                               |
+=============================+=====================================+
|  Number of games processed  |                                     |
+-----------------------------+-------------------------------------+
|  Size of games processed    | GB                                  |
+-----------------------------+-------------------------------------+
|  Number of observations     |                                     |
+-----------------------------+-------------------------------------+
|  Size of observations       | GB                                  |
+-----------------------------+-------------------------------------+


The Tricky Bit
^^^^^^^^^^^^^^^^
The size of the database is considerable, and difficult to fit onto RAM all at
once. It becomes necessary then to split the database to be loaded to RAM 
piecemeal. This presents a few issues, particularly when batching data:

* RAM usage must remain stable as one piece finishes and the next is loaded.
* Multiprocessing must remain possible to expedite batching


Machine Learning Engineering
------------------------------

Supervised Learning
^^^^^^^^^^^^^^^^^^^^^

**Autoencoding-**

**Classification-**

**MiniMax Search-**

Reinforcement Learning
^^^^^^^^^^^^^^^^^^^^^^^^

Generative Model
^^^^^^^^^^^^^^^^^

