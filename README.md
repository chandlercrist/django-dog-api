# Dog API

Django REST framework assignment with Dog and Breed CRUD APIs. Both slash and no-slash URLs work. The initial commit uses explicit APIView classes; the bonus commit replaces them with ModelViewSets.

## Start (macOS / Linux, Python 3.10+)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Run automated tests with `python manage.py test`. SQLite is created by migrate; the database is intentionally not committed. This is an unauthenticated local classroom application; do not deploy it publicly as configured.

## Routes

| URL | Methods |
| --- | --- |
| `/api/dogs/` | GET list, POST create |
| `/api/dogs/<id>` | GET retrieve, PUT full update, DELETE |
| `/api/breeds/` | GET list, POST create |
| `/api/breeds/<id>` | GET retrieve, PUT full update, DELETE |

Dog `breed` is a numeric Breed ID. Create the breed first. Sizes are case-sensitive Tiny, Small, Medium, Large. Ratings are integers 1–5. Age must be nonnegative. Invalid data returns 400; missing IDs return 404. Successful creation returns 201; retrieval/update 200; deletion 204 with no response body. Delete dogs before their breed; a referenced breed returns 409 to prevent accidental dog deletion.

## Postman evidence

Import `postman/Dog_API.postman_collection.json`. Start the Django server, then send requests 01–10 in order. POST tests automatically save the IDs used in later requests. Take one screenshot after each request showing its method, full URL, response status, and response body (empty for DELETE). For POST/PUT also show the JSON request body where practical. Save screenshots as 01.png through 10.png. Do not rerun DELETE before capturing its successful 204 response. The collection is reusable: each run creates new records and removes them at the end.

Automated test output is not a substitute for the instructor's requested Postman screenshots.

## GitHub publication

Create an empty repository named `django-dog-api` on GitHub. Do not initialize it with README, license, or gitignore because this project already has history. Extract the project ZIP, including its `.git` directory, then run:

```bash
git remote add origin https://github.com/YOUR_USERNAME/django-dog-api.git
git push -u origin main
git push origin --tags
```

If an origin already exists, inspect it with `git remote -v` before changing it. Authenticate with your own GitHub account; do not place access tokens in project files.

The ZIP preserves both commits and tags. `git show v1-class-based:dogapi/controllers.py` shows the initial implementation. `git checkout v1-class-based` lets you run it; `git switch main` returns to the bonus viewset version. Commit hashes and submission link templates are supplied in `SUBMISSION.md` in the final package.

## References

- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
- https://www.django-rest-framework.org/tutorial/3-class-based-views/
- https://www.django-rest-framework.org/api-guide/viewsets/
