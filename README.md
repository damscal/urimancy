# Urimancy

*The art of unbreakable references.*

## Motivation
Naming things is famously "one of the hard problems" in computer science.
Even harder, it is to quickly come up with a whole hierarchical tree of file paths that cannot ever be changed later on the way,
unless dealing with a whole lot of broken references.  
At the same time, people traditionally try to use filesystem trees to semantically organize and browse files,
yet trees are not much suitable for that purpose (compared to databases). There are filesystem links, but they are tedious and suboptimal (again, compared to databases). 

The idea is then to stop trying to come up with more and more sophisticated hierarchies to organize files.   
One simple hierarchy shall suffice (for storing purposes),
while databases can take care of the retrieval part. 

## Core concept

```mermaid
flowchart
  node_1("You place a file or a folder 'F'<br> into a directory 'D'<br> monitored by the Urimancy service daemon.")
  node_2("The file/folder 'F' gets copied in the associated Urimancy Store 'S'")
  node_3("The file/folder 'F' in the directory 'D'<br> gets replaced by a link 'L'.")
  node_4("You are free to rename, copy, move or delete the link 'L',<br> as well as the content of the file/folder 'F'.")
  node_5("If you don#39;t need <br> #39;L#39; anymore...")
  node_6("You can just<br> delete it.")
  node_7("If you don#39;t need <br>#39;F#39; anymore...")
  node_8("Delete all links pointing to #39;F#39;.<br> #39;F#39; will be automatically<br>deleted at that point.")
  node_9("You also have the option to delete #39;F#39;<br> along with all links pointing to it<br>with one advanced command.")
  node_10("As long #39;F#39; exists,<br> it will always be accessible <br> via its static path<br> in its Urimancy Store.")
  node_11["You associate a directory (or a set of directories) with an Urimancy Store 'S'.<br> Urimancy will start monitoring 'D' for filesystem changes."]
  node_12["Urimancy Stores also can record tags<br> and other files' metadata,<br> providing a backbone for advanced browsing,<br> searching and querying interfaces."]
  node_1 --> node_2
  node_2 --> node_3
  node_3 --> node_4
  node_4 --> node_5
  node_5 --> node_6
  node_4 --> node_7
  node_7 --> node_8
  node_7 --> node_9
  node_4 --> node_10
  node_11 --> node_1
  node_10 --> node_12
```
