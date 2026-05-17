## Task 1
- An ELI5-style explanation of what it represents physically
- Whether it's a single-level variable (e.g. surface temperature) or one associated with pressure levels (e.g. wind at different altitudes in the atmosphere)
- Common abbreviation(s) for the variable

The wind speed is how fast the wind is blowing (without the direction). In this project's case, we use the wind speed at 10 meters, which is a a single-level variable since it only measures at 10 meters. 

Common abbreviations:
- 10m wind speed, 10m_wind_speed

## Task 2
![Wind Animation](wind_animation.gif)

- I chose a matplotlib animation because it can be exported into a gif using `pillow`! (The animation is quite heavy on the GPU...)
## Task 3
Questions:
1. 6 hours
2. UTC
3. the number of points across the longitude x latitude
4. a chunked array storage format for large datasets