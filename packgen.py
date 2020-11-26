# Generator used for all the Skinned Lanterns lantern variants!

lanterns = ["pufferfish", "zombie", "creeper", "skeleton", "wither_skeleton",
"bee", "jack_o_lantern", "ghost", "inky", "pinky", "blinky", "clyde", "pacman",
"paper_white", "paper_yellow", "paper_orange", "paper_blue", "paper_light_blue",
"paper_cyan", "paper_lime", "paper_green", "paper_red", "paper_pink",
"paper_brown", "paper_black", "paper_gray", "paper_light_gray", "paper_magenta",
"paper_purple", "guardian"]

shader_path = "assets/skinnedlanterns/materialmaps/"
handheld_path = "assets/skinnedlanterns/lights/item/"

material = """
{{
  	"defaultMaterial": "canvas:{type}_glow",

  	"variants": {{
        "facing=north,hanging=false,waterlogged=true": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=north,hanging=false,waterlogged=false": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=north,hanging=true,waterlogged=true": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=north,hanging=true,waterlogged=false": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=east,hanging=false,waterlogged=true": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=east,hanging=false,waterlogged=false": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=east,hanging=true,waterlogged=true": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=east,hanging=true,waterlogged=false": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=south,hanging=false,waterlogged=true": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=south,hanging=false,waterlogged=false": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=south,hanging=true,waterlogged=true": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=south,hanging=true,waterlogged=false": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=west,hanging=false,waterlogged=true": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=west,hanging=false,waterlogged=false": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=west,hanging=true,waterlogged=true": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=west,hanging=true,waterlogged=false": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=up,hanging=false,waterlogged=true": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=up,hanging=false,waterlogged=false": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=up,hanging=true,waterlogged=true": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=up,hanging=true,waterlogged=false": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=down,hanging=false,waterlogged=true": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=down,hanging=false,waterlogged=false": {{ "defaultMaterial": "canvas:{type}_glow" }},
        "facing=down,hanging=true,waterlogged=true": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }},
        "facing=down,hanging=true,waterlogged=false": {{ "defaultMaterial": "swingchain:swinging_{type}_glow" }}
  	}}
}}
"""

normal_light = """
{
  "intensity": 0.93,
  "red": 1.0,
  "green": 1.0,
  "blue": 0.8,
  "worksInFluid": false
}
"""

soul_light = """
{
  "intensity": 0.93,
  "red": 0.6,
  "green": 0.8,
  "blue": 1.0,
  "worksInFluid": true
}
"""

for lantern in lanterns:
    normal = open(shader_path + "block/" + lantern + "_lantern_block.json", "w")
    soul = open(shader_path + "block/" + lantern + "_soul_lantern_block.json", "w")
    normal_item = open(shader_path + "item/" + lantern + "_lantern_block.json", "w")
    soul_item = open(shader_path + "item/" + lantern + "_soul_lantern_block.json", "w")
    normal_handheld = open(handheld_path + lantern + "_lantern_block.json", "w")
    soul_handheld = open(handheld_path + lantern + "_soul_lantern_block.json", "w")
    normal.write(material.format(type = "warm"))
    soul.write(material.format(type = "luminance"))
    normal_item.write("{}")
    soul_item.write("{}")
    normal_handheld.write(normal_light)
    soul_handheld.write(soul_light)
    normal.close()
    soul.close()
    normal_item.close()
    soul_item.close()
    normal_handheld.close()
    soul_handheld.close()

print("Filegen complete!")
