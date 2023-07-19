# rockband2manualAP
Implementation of Rock Band 2 into Archipelago Manual

**Game:** Rock Band 2

**Checks:** Each chart from every song in the game.

**Key Items:** Song unlocks and Progressive Tier unlocks.

**Other Items:** Overdrive and use of Hyper Speed as unlockables.

**Victory Condition:** Up in the air, but focused around songs in Tier 6. Whether it's an FC goal (such as 20 Tier 6 FCs) or a Star goal (50 Stars from Tier 6), it can be dependant on your skill level and time committment.

**Notes:** Implementation of this is pretty basic, which makes it compatible with other RB2-related games with the same setlist, such as RB3 or YARG. There are six Progressive Tier unlocks that unlock each tier past the very first tier (0 dot). All of the tiering is based off of the band tier from Rock Band 2 - this tiering may differ if you decide to play this in a different game other than RB3. In that case, refer to the tiering listed in the "Items Received" section of the Manual client.

Since you will need to start with songs to be able to actually play the game, I have included 4 yaml options that give you a random set of 3 songs from tier 0. I have also included versions of those 4 options that exclude *all** the drum charts from containing key items. Mostly because drums are a little harder to come by/more expensive, so I am just trying to avoid that barrier of entry. You can also change these options to exclude other instruments as you desire, such as vocals (especially if you decide to play this using Clone Hero, which has no vocals support). Keep in mind you will need at least two instruments available to fit all the key items, or generation will fail.
