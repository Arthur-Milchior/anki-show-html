# Description
Allows to view HTML of each field of the selected card. Go to the
browser, select some notes, go to edit->"Note's HTML". For each
selected note, you'll have a text showing the fields and their
html. This text is also printed of the standard output (assuming you
launched anki from a terminal).
# Rational
This allows you to understand why a field which appear to be empty is
not, to view the name of an image, to view that some tags are opened
and not closed (or reciprocally)... i.e. I use it to debug my cards
when I've strange problem

## Warning:

Do not use this add-on on cards which are in Filtered decks. You'll
have a warning message and I don't know what the result will be. I'm
however sure that, in the best case, it won't do anything, in the
worst, it will mess with your collection. And honestly, I don't care
enough about this bug to correct it.

## Anki > 2.1.20
Anki changed a lot in version 2.1.20. I am currently unable to
understand those change, as they are in rust, and I don't know
it. Furthermore, rules for card generation change, so it's possible
that this add-on becomes useless. Anyway, until I know more about
2.1.20, this add-on won't be available with latest anki. As this
add-on as only peen downloaded 63 times, I believe that's not a real trouble.

Note that you can use "ctrl+shift+x" to access the html content of a field.
## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   |Arthur Milchior <arthur@milchior.fr>
Based on    |Anki code by Damien Elmes <anki@ichi2.net>
License     |GNU AGPL, version 3 or later; http|//www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-show-html
Addon number| [1778098423](https://ankiweb.net/shared/info/1778098423)
Support me on| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](https://Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
