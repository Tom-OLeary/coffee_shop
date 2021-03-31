# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project


1) Displays graphics representing the ratios of ingredients in each drink.
2) Allows public users to view drink names and graphics.
3) Allows the shop baristas to see the recipe information.
4) Allows the shop managers to create new drinks and edit existing drinks.

## Auth0 Information
* AUTH0_DOMAIN = 'tom-o.us.auth0.com'
* ALGORITHMS = ['RS256']
* API_AUDIENCE = coffee

### Barista
* Username: barista@fullstack.com
* Password: Barista1!
* JWT = ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxoSlppRHhyZE9ZWkFQWVdOUGlvdyJ9.eyJpc3MiOiJodHRwczovL3RvbS1vLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDNkMjRkNzRiNDk3OTAwNjkyNjNmNjUiLCJhdWQiOiJjb2ZmZWUiLCJpYXQiOjE2MTcwNDE5MTAsImV4cCI6MTYxNzA0OTExMCwiYXpwIjoiT21Sd0dDRGlXcWw5RkJiUE1paGJkNXU2UXFSSlc3WDEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MtZGV0YWlsIl19.LJj-8xRSmaa6TJitjwwxhQ0hHBffJmkgvNhvZrCFZRQLKjpoXFyH3AMMRDrwnJbQDySGq4cjgHcZJrI9fnojjIk84fQ27knofGZQ8sK1hAOPsbnGfLI5Ks2Z8CvYsN3_SfPeuO6Jxb_r4WF3kp6mTIp3g5uTJwgQDBEjiReVeAVcDKhhrW8Rz8rB9zWY-mkWavPdoCl95XkTxgYAtAj4wl1X3D7SpFoUnC0m-Ht7lRdiGk_RXeITJRGHQE0PjNa2wnjW1eV_aDaTsaNhoTANRfwWZ-3bnQH50btszmtsCoVZGr1jGP-z2qNRYXJ2AZjD7dTmLZPsm-KO_gL7FwPfGQ```

### Manager
* Username: manager@fullstack.com
* Password: Manager1!
* JWT = ```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkxoSlppRHhyZE9ZWkFQWVdOUGlvdyJ9.eyJpc3MiOiJodHRwczovL3RvbS1vLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDNkMjRhZGViNGQ2MDAwNzBmZjJmMjciLCJhdWQiOiJjb2ZmZWUiLCJpYXQiOjE2MTcwNDE4ODIsImV4cCI6MTYxNzA0OTA4MiwiYXpwIjoiT21Sd0dDRGlXcWw5RkJiUE1paGJkNXU2UXFSSlc3WDEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCIsInBhdGNoOmRyaW5rcyIsInBvc3Q6ZHJpbmtzIl19.EHfMTC4f1-ihRvf1msmZEc5lp6kIBA02OqR9lvUyOM3bYrH9Z1u3h7vSim_PNy5TcYkDXMg9B3oINPArYbQ5gA7IHHpoaz3oq36AYmXqMIPQXK7j0fKtrqmyJPeYgD8tXP7aAZxlrmV2UNbJwrNJ10uSTb3o0Z9vNNBYhMIm9MRMiJsu3lzX1xX6sJqhjNbB9Lmv7HrczGAl0mC9_sKEylZ9vJ9dbyMMrUt0bh4apjyb9EsRJw_I7dm6O1dbtAUm-71C0wlsXTsAqPX5Tk7_GRuNJvn7483_NTJBgR3YOtBJgSXT5FaUR76ooWdsHo1FIFMhRGgz83ED2VEoZV1Baw```

## Additional README Files

There are `@TODO` comments throughout the project. We recommend tackling the sections in order. Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

## About the Stack

### Backend

The `./backend` directory contains a Flask server with an SQLAlchemy module. Contains the endpoints, configure and 
Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains an Ionic frontend to consume the data from the Flask server. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

    let link = 'https://';
    link += this.url + '.auth0.com';
    link += '/authorize?';
    link += 'audience=' + this.audience + '&';
    link += 'response_type=token&';
    link += 'client_id=' + this.clientId + '&';
