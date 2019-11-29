graph [
  directed 1
  node [
    id 0
    label "Hacked"
  ]
  node [
    id 1
    label "Bug"
  ]
  node [
    id 2
    label "Malware"
  ]
  node [
    id 3
    label "Outcome"
  ]
  node [
    id 4
    label "Physical"
  ]
  node [
    id 5
    label "Misuse"
  ]
  node [
    id 6
    label "Error"
  ]
  node [
    id 7
    label "Environment"
  ]
  node [
    id 8
    label "Social"
  ]
  edge [
    source 0
    target 1
    weight 0.5
  ]
  edge [
    source 0
    target 3
    weight 0.8
  ]
  edge [
    source 1
    target 3
    weight 0.75
  ]
  edge [
    source 2
    target 1
    weight 0.75
  ]
  edge [
    source 2
    target 3
    weight 0.7
  ]
  edge [
    source 4
    target 3
    weight 0.3
  ]
  edge [
    source 5
    target 3
    weight 0.5
  ]
  edge [
    source 6
    target 3
    weight 0.4
  ]
  edge [
    source 7
    target 3
    weight 0.6
  ]
  edge [
    source 8
    target 3
    weight 0.2
  ]
]
