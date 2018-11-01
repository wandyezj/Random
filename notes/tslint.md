# tslint

##
```json
    "tslint": "./node_modules/.bin/tslint --project ./tsconfig.json"
```

## Preferred  tsconfig.json

```json
{
    "defaultSeverity": "warning",
    "extends": ["tslint:recommended", "tslint-config-prettier"],
    "jsRules": {},
    "rules": {
        "object-literal-sort-keys": false,
        "object-literal-shorthand": false,
        "interface-name": [true, "never-prefix"]
    },
    "rulesDirectory": [],
    "linterOptions": {
        "exclude": [
            "dist",
            "*.js",
            "*.json"
        ]
    }
}
```


## Annoying Rules


* [Interface name](https://palantir.github.io/tslint/rules/interface-name/)
    * Having interfaces start with I is annoying.