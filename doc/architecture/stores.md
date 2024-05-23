# Stores

## Positioning and Naming Urimancy stores

Urimancy stores can be initialized anywhere the user has write access to. However, once a store is placed and used, it cannot be moved or renamed without inevitably breaking all the references that rely on that store.  
By default, Urimancy stores are placed in `~/.urimancy` for user instances and/or `/etc/urimancy` for system instances.

Similarly, stores can be given any name, but that name should not be changed afterwards.  
By default, stores that share the same location are named progressively as `store-1`, `store-2`, etc. 

### Additional names and locations

Notably, stores can (virtually) have several locations and names, as it is sufficient to create symlink directories pointing to the real store path.

#### Example:  
if the real path to a store is `~/.urimancy/store-1`, nothing stops you from creating a symlink `~/myUrimancyStores/SSD-store` pointing to `store-1`, effectively providing a new (virtual) location and name to the store.  
Again, this new name and location cannot be easily revoked in the future, if there are any references using them.


## Internal structure

### Schema:

* `<Urimancy Store Name>`
    * `<year>`
        * `<month>`
            * `<day>`
                * `<immutable filename>`

#### Example:
The following is a practical example of a file originally called **README.md**, stored in **store-1** on **July 29th, 2024** at standard time **21.30**:

`<path/to/store-1>/store-1/2024/07/29/21.30-README.md`
