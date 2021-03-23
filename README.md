
```gitexclude
git init
git status
git add .
git commit -m 'message'
```

### a way to get data `model_set`
    # this withh get all post of user pk = 1
    User.objects.get(pk=1).post_set.all()

### create a new post
    # no need for save() it already created nd saved in thee same time
    User.objects.get(pk=2).post_set.create(author = 'name', title = 'home')