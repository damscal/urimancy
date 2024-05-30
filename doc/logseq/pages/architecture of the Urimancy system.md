- ```mermaid
  flowchart
  subgraph Server
    subgraph interfaces
    end
    subgraph daemon
    end
    subgraph writing_agent[writing agent]
    end
  end
  subgraph client
  end
  subgraph stores[Urimancy Stores]
    subgraph store1
    end
    subgraph store2
    end
  end
  interfaces -->|purpose| interfaces_purpose(["handles requests <br>and configurations"])
  client -->|requests & config| interfaces
  interfaces & daemon -->|signal| writing_agent -->|writes to| stores
  daemon -->|purpose|daemon_purpose(["trigger routines, <br>repetitive tasks"])
  ```
-