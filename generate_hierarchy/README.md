This folder details how to generate a simple hierarchy that can be used to populate our DB analytics bot's prompt.

- all the function generate_hierarchy() requires is that 'config' exisits in the correct format in the **required_files** folder.

**note:**
* For production databases this hierarchy will typically not be enough (unless you have very clean tables with neatly
defined keys, and highly logical column names.)
  * to create a more detailed hierarchy that includes this information you can make use of any SQL code that is laying around 
    to infer more knowledge about tables, columns, and how to query and join them together. When i get around to it i will 
    add this functionality to this repository.
 * it is also worth noting that high quality, data-base specific examples are tremendous in helping the llm understand 
how to effectivly query complex databases. consider methods for dynamically populating your prompts with examples that are specific
to the tables the user wants to be using.. 

an example output of the function is shown below.

generate_hierarchy('./config.yaml')
**output:**
   - "my actual uri that the llm will use for creating connections."
      - production
         - brands
            - brand_id, INTEGER
            - brand_name, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
         - categories
            - category_id, INTEGER
            - category_name, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
         - products
            - product_id, INTEGER
            - product_name, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - brand_id, INTEGER
            - category_id, INTEGER
            - model_year, SMALLINT
            - list_price, DECIMAL(10, 2)
         - stocks
            - store_id, INTEGER
            - product_id, INTEGER
            - quantity, INTEGER
      - sales
         - customers
            - customer_id, INTEGER
            - first_name, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - last_name, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - phone, VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - email, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - street, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - city, VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - state, VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - zip_code, VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS"
         - order_items
            - order_id, INTEGER
            - item_id, INTEGER
            - product_id, INTEGER
            - quantity, INTEGER
            - list_price, DECIMAL(10, 2)
            - discount, DECIMAL(4, 2)
         - orders
            - order_id, INTEGER
            - customer_id, INTEGER
            - order_status, TINYINT
            - order_date, DATE
            - required_date, DATE
            - shipped_date, DATE
            - store_id, INTEGER
            - staff_id, INTEGER
         - staffs
            - staff_id, INTEGER
            - first_name, VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - last_name, VARCHAR(50) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - email, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - phone, VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - active, TINYINT
            - store_id, INTEGER
            - manager_id, INTEGER
         - stores
            - store_id, INTEGER
            - store_name, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - phone, VARCHAR(25) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - email, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - street, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - city, VARCHAR(255) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - state, VARCHAR(10) COLLATE "SQL_Latin1_General_CP1_CI_AS"
            - zip_code, VARCHAR(5) COLLATE "SQL_Latin1_General_CP1_CI_AS"



