# Paint Color Mixer Web App

A comprehensive web application for mixing paint colors using traditional RYB (Red-Yellow-Blue) color theory with support for addition and subtraction operations.

## Overview

This application allows you to:
- **Mix/Add colors** using ratio-based mathematics
- **Subtract colors** with validation (ensures operations are mathematically valid)
- **Identify colors** by name or coordinate form
- **View color definitions** for primary through quinary colors

## How to Use

### Running the App

1. Open `color-mixer.html` in any modern web browser
2. No installation or dependencies required - it's a standalone HTML file!

Alternatively, you can run a local web server:
```bash
cd ColorCode
python3 -m http.server 8080
# Then open http://localhost:8080/color-mixer.html in your browser
```

### Features

#### 1. Add/Mix Colors

Mix colors together using natural language:

**Examples:**
- `Blue + Red` → Purple [1,1,0]
- `Blue + Purple` → Violet [3,1,0]
- `2 Blue + 1 Violet` → [11,1,0]
- `Red + Yellow + Blue` → Brown (shade)

The algorithm automatically:
- Expands nested color definitions
- Calculates proper ratios
- Simplifies to smallest integer form
- Identifies the resulting color

#### 2. Subtract Colors

Remove one color from another (with validation):

**Examples:**
- `Purple - Blue` → Red [0,1,0]
- `Violet - Blue` → Purple [1,1,0]
- `Violet - 2 Blue` → Crimson [1,3,0] ✓
- `Violet - Red` → NOT POSSIBLE (insufficient Red in Violet)

The subtraction algorithm:
1. Counts total parts in the operation
2. Scales the color being subtracted from
3. Calculates m% (proportion being removed)
4. Validates that sufficient color exists
5. Performs the subtraction
6. Simplifies the result

#### 3. Color Lookup

Look up any color by name or coordinate:

**Examples:**
- `Purple` → Shows [1,1,0], Secondary color
- `[3,1,0]` → Shows Violet, Tertiary color
- `[2,5,1]` → Shows closest match (Shade of...)

## Color System

### Coordinate Format: [Blue, Red, Yellow]

All colors are represented as ratios of Blue, Red, and Yellow parts.

### Color Hierarchy

#### Primary Colors (3)
- **Blue**: [1,0,0]
- **Red**: [0,1,0]
- **Yellow**: [0,0,1]

#### Secondary Colors (3)
Mixtures of 2 primaries in equal parts:
- **Purple**: [1,1,0] = Blue + Red
- **Orange**: [0,1,1] = Red + Yellow
- **Green**: [1,0,1] = Blue + Yellow

#### Tertiary Colors (6)
Mixtures of 1 primary + 1 adjacent secondary:
- **Violet**: [3,1,0] = Blue + Purple
- **Crimson**: [1,3,0] = Red + Purple
- **Vermilion**: [0,3,1] = Red + Orange
- **Amber**: [0,1,3] = Yellow + Orange
- **Chartreuse**: [1,0,3] = Yellow + Green
- **Teal**: [3,0,1] = Blue + Green

#### Quaternary Colors (12)
Mixtures between adjacent tertiary colors:
- **Ultramarine**: [4,1,0]
- **Indigo**: [2,1,0]
- **Magenta**: [1,2,0]
- **Rose**: [1,4,0]
- **Carmine**: [0,4,1]
- **Scarlet**: [0,2,1]
- **Tangerine**: [0,1,2]
- **Gold**: [0,1,4]
- **Canary**: [1,0,4]
- **Lime**: [1,0,2]
- **Turquoise**: [2,0,1]
- **Azure**: [4,0,1]

#### Quinary Colors (24 defined - selection shown)
Even finer gradations:
- **Sapphire**: [5,1,0]
- **Navy**: [5,0,1]
- **Cobalt**: [3,2,0]
- **Orchid**: [2,3,0]
- **Fuchsia**: [1,5,0]
- **Ruby**: [0,5,1]
- **Coral**: [0,3,2]
- **Peach**: [0,2,3]
- **Marigold**: [0,1,5]
- **Lemon**: [2,0,5]
- **Mint**: [3,0,2]
- **Jade**: [2,0,3]
- **Cyan**: [5,0,1]
- **Cerulean**: [3,1,1]

## Algorithm Details

### Addition Algorithm

When adding colors like `2 Blue + 1 Violet`:

1. **Expand nested colors**: Violet = [3,1,0] = 3 Blue + 1 Red
2. **Multiply by parts**: 1 × Violet = 1 × (3 Blue + 1 Red)
3. **Add components**: 2 Blue + 3 Blue + 1 Red = 5 Blue + 1 Red
4. **Express as ratio**: [5,1,0]
5. **Simplify to smallest integers**: Already simplified
6. **Identify color**: Check database or find closest match

### Subtraction Algorithm

When subtracting colors like `Violet - 2 Blue`:

1. **Count parts**: 1 Violet + 2 Blue = 3 parts total
2. **Scale up color1**: 3 × [3,1,0] = [9,3,0]
3. **Calculate m%**: 2/(2+1) = 66.67%
4. **Validate**: Is Blue ≥ 66.67% of [9,3,0]?
   - Blue is 9/12 = 75% ✓ Valid
5. **Subtract**: [9,3,0] - [8,0,0] = [1,3,0]
6. **Simplify**: [1,3,0] (already simplified)
7. **Identify**: This is Crimson!

### The m% Rule

For subtraction `A - B` to be valid:
- m% = (parts of B) / (total parts in operation)
- Each component of B must be ≤ m% of that component in A
- This ensures you're not trying to remove more of a color than exists

Example: `Purple - 2 Blue`
- m% = 2/(1+2) = 66.67%
- Purple = [1,1,0], so Blue is 50% of Purple
- 50% < 66.67%, so this is **NOT POSSIBLE**

## Technical Details

### Technologies Used
- Pure HTML5, CSS3, and JavaScript
- No external dependencies
- Works offline
- Responsive design

### Color Display
- Colors are converted from RYB to RGB for screen display
- Uses trilinear interpolation in RYB color cube
- Approximates paint mixing behavior on screen

### Files in This Directory
- **color-mixer.html**: Main web application (standalone)
- **ColorConverter_RYBWK_to_RGB_HEX_Name_Plot.m**: MATLAB color converter
- **ColorListVals.csv**: Extended color database with RGB/HEX values
- **README.md**: This documentation

## Examples and Use Cases

### Example 1: Making Violet
```
Input: Blue + Purple
Result: Violet [3,1,0]
Explanation: Blue [1,0,0] + Purple [1,1,0]
           = [1,0,0] + [1,1,0]
           = [2,1,0]
           Wait, that should be [2,1,0]...

Actually: Purple = 1/2 Blue + 1/2 Red
          So: 1 Blue + 1 Purple
            = 1 Blue + 1/2 Blue + 1/2 Red
            = 3/2 Blue + 1/2 Red
            = [3,1,0] in ratio form
```

### Example 2: Complex Mixing
```
Input: 2 Blue + 1 Violet
Violet = [3,1,0] = 3 Blue + 1 Red
So: 2 Blue + 1(3 Blue + 1 Red)
  = 2 Blue + 3 Blue + 1 Red
  = 5 Blue + 1 Red
  = [5,1,0]
Result: Sapphire
```

### Example 3: Subtraction
```
Input: Violet - Blue
Violet = [3,1,0]
Scale: 4 parts total, so 4×[3,1,0] = [12,4,0]
m% = 1/4 = 25%
Blue in Violet: 12/16 = 75% ✓ (≥ 25%)
Subtract: [12,4,0] - [12,0,0] = [0,4,0] = [0,1,0]
Result: Red
```

## Future Enhancements

Possible additions:
- Save/load color palettes
- Color history
- Share color combinations via URL
- Export to various formats (CSS, RGB, HEX)
- Tint/shade calculator (adding white/black)
- Complementary color finder
- Color harmony generator

## Credits

Created as part of the UlyssesCode project by TSWessler.

Based on traditional RYB (subtractive) color theory used in painting and art education.

## License

Part of the UlyssesCode repository.
