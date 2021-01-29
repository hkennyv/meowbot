# functions

The directory containing the source code to wrap the trained language models
into a python lambda.

It uses the same dependencies as the parent dir, so you can

```
pip install -r ../requirements.txt
```

## Testing

To test the function, you can use the function-framework to run a dev server
locally. Make sure you're in the `models/functions` directory and then use:

```
function-framework --target handler --debug
```

The dev server should be live at <http://localhost:8080> where you can make
requests to.
