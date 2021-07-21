## Elasticsearch

#### create and populate the Elasticsearch index and mapping
```
python manage.py search_index --rebuild
```

#### how to search
```
http://127.0.0.1:8000/api/search?search=keyword
http://127.0.0.1:8000/api/search?search=keyword&query=value#link=somelink
```
