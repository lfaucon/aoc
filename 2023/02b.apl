⎕IO←0
s←{⍵⊆⍨⍺≢¨⍵}
⎕←+/{×/(1⊃¨⍵){⌈/⍎¨⍵}⌸⊃¨⍵}¨{{' 's¨⍵}','s', '⎕R','(';'⎕R',')1⊃':'s⍵}¨⊃⎕NGET'2.txt' 1