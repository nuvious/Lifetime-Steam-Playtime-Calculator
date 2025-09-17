# Lifetime Steam Game Playtime Calculator

This is just a quick script to calculate your lifetime steam game playtime. This works in general
but particularly if you and your friends have private profiles that public profile calculators will
not be able to see.

## Instructions

- Go to your profile or a friend's profile.
- Click on `Games` link on the right, should bring you to the `All Games` tab.
- Copy everything using CTRL-A + CTRL-C
- Paste into file named `steam_time.txt` in the same directory as the python script.
- Run the script.

## Example Output

There's an example file for `steam_time.txt` in this repo. This is the output from that sample file:

```bash
$ python ./lifetime_steam_time.py
Total Steam Time: 0 year(s) 88 day(s) 0 hour(s) 6 minute(s)
```

## Limitations

Some apps in Steam like Blender may be left open for long periods of time skewing results. Other
games have companion apps like VRChat and OVR Advanced Toolkit that double, triple, etc the
playtime this calculates. You can edit the script to subtract out these multiplications of time
manually as long as you do it in units of minutes.

For example starting at line 35 you could enter:

```python
# Subtract out blender gametime
total -= 1000 * 60

# Subtract out OVR Advanced Toolkit
total -= 125.3 * 60
```
