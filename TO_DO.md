For example, in a Flask app, you may use unit tests to test:

    Database models
    Utility functions that your view functions call

Functional tests, meanwhile, should focus on how the view functions operate.

For example:
### (Attempt) to Capture Plan for tests:

- [ ] 1. Nominal conditions (GET, POST, etc.) for a view function.
- [ ] 2. Invalid HTTP methods are handled properly for a view function.
- [ ] 3. Invalid data is passed to a view function.xw
