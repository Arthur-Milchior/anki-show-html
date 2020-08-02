# Select any number of cards in the card browser and add/remove a prefix to their deck name.

## Usage:

1. Open the card browser
2. Select the desired cards
3. Go to "Edit > Add prefix"(Ctrl+Alt+P)/"Remove prefix"(Ctrl+Alt+Shift+P)


## Rationales

My main goal was: exporting some cards selected in the browser. (This
can now be done using add-on [1983204951:Export cards selected in the
Browser](https://ankiweb.net/shared/info/1983204951).)

In order to do this, I add a common prefix to all of cards I want to
export. In the main window, I export this deck. Once I import the deck
again, I just delete this prefix, and everything go back in the
initial deck.

It leaves an empty deck "prefix" which can quickly and easily be
removed.

## TODO
Allow to directly export notes by selecting them in the browser

Key         |Value
------------|-------------------------------------------------------------------
Copyright   |Arthur Milchior <arthur@milchior.fr>
Based on    |Anki code by Damien Elmes <anki@ichi2.net>
License     |GNU AGPL, version 3 or later; http|//www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-show-html
Addon number| [1262882834](https://ankiweb.net/shared/info/1262882834)
