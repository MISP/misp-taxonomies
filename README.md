# MISP Taxonomies

Taxonomies that can be used in MISP and other information sharing tool and expressed in Machine Tags (Triple Tags). A machine tag is composed of a namespace (MUST), a predicate (MUST) and an (OPTIONAL) value. Machine tags are often called triple tag due to their format.

The following taxonomies can be used in MISP (as local or distributed tags) or in other tools willing to share common taxonomies among security information sharing tools.

## [Admiralty Scale](./admiralty-scale)

The Admiralty Scale (also called the NATO System) is used to rank the reliability of a source and the credibility of an information.

# MISP Taxonomies - tools

[machinetag.py](./tools/machinetag.py) is a parsing tool to dump taxonomies expressed in Machine Tags (Triple Tags) and list all valid tags from a specific taxonomy.

~~~~shell
% cd tools
% python machinetag.py 
        admiralty-scale:source-reliability="a"
        admiralty-scale:source-reliability="b"
        admiralty-scale:source-reliability="c"
        admiralty-scale:source-reliability="d"
        admiralty-scale:source-reliability="e"
        admiralty-scale:source-reliability="f"
        admiralty-scale:information-credibility="1"
        admiralty-scale:information-credibility="2"
        admiralty-scale:information-credibility="3"
        admiralty-scale:information-credibility="4"
        admiralty-scale:information-credibility="5"
        admiralty-scale:information-credibility="6"
        ...
~~~~

