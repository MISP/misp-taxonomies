# Binary Classification

Custom taxonomy for tagging of known binary files

## type

<dl>
<dt>good</dt>
<dd>Known good/safe</dd>
<dt>bad</dt>
<dd>Known bad/malicious<dd>
<dt>unknown</dt>
<dd>Not yet known</dd>
</dl>

# Machine-parsable Binary Taxonomy

The repository contains a [JSON file including the machine-parsable tags](machinetag.json)
along with their human-readable description. The software can use both
representation on the user-interface and store the tag as machine-parsable.

~~~~
binary-class:type="good"
~~~~

