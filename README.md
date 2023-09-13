# Flask_SQlite_DB
Python Flask web service that manages users and their blog posts using sqlite Database

The application uses Flask, a web framework, and SQLAlchemy, an Object-Relational Mapping (ORM) library, to interact with a SQLite database. It defines two main models: User and BlogPost, representing users and their blog posts. Also, this application demonstrates various data structures and algorithms, such as linked lists for user management in database, binary search trees for efficient blog post retrieval from database, and stacks for batch deletion in database. It combines these concepts to build a functional web service for managing users and their blog posts.
Creating Users: You can create new user profiles with their names, email addresses, home addresses, and phone numbers. When you hit the "Create" button, it saves this information.

**
This code includes configurations to ensure SQLite enforces foreign key constraints.
**
- /user (POST): Allows the creation of a new user by accepting JSON data with user details and storing it in the database.

- /user/descending_id and /user/ascending_id (GET): Retrieve all users, ordering them either in descending or ascending order of their IDs, and return the data as JSON.

- /user/<user_id> (GET and DELETE): Get details or delete a specific user by their ID.

- /blog_post/<user_id> (POST): Create a new blog post associated with a user. It performs hashing on the data and stores it in the database.

- /blog_post/<blog_post_id> (GET): Retrieve a specific blog post by its ID using a binary search tree for efficient lookup.

- /blog_post/numeric_body (GET): Retrieve all blog posts with their text bodies transformed into numeric values by summing the ASCII values of characters.

- /blog_post/delete_last_10 (DELETE): Delete the last 10 blog posts using a stack data structure for efficient removal.
