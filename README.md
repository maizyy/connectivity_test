# Connectivity Test
Python script made for testing connections from one machine to others

**Warning**
Script will only work correctly with `config.json` file. Below is a schema that script will understend

```json
{
    "service_name": {
        "addresses": "x.x.x.x x.x.x.x",
        "ports": "22",
        "skip": true, // (optional) test will be performed in upd mode, if this key is present [can be any value]
        "udp": true // (optional) test will be performed in upd mode, if this key is present [can be any value]
    },
    "service_name2": {
        ...
    },
}
```