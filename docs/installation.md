# Installation and Setup

{% hint style='tip' %}
If you are a new Python developer, or are unsure what pip even is, try starting [here](https://packaging.python.org/installing/).
{% endhint %}

The easiest way to install the base version of orca is through Python's [pip](https://pip.pypa.io/en/stable/) utility. To simply install the most minimal version of orca, simply run:

```sh
pip install orca-py
```

## Optional Dependencies

orca provides a set of optional dependencies which add various bits of functionality or performance changes when installed. These can all be installed in a similar fashion to orca;

```sh
pip install orca-py[performance]
```

| Name | Explanation | Versions |
|------|-------------|----------|
| voice | Adds functionality required to connect and use voice | Both |
| http | Adds a built-in HTTP server w/ Flask, allowing plugins to handle HTTP requests | Both |
| music | Adds the ability to stream and play music from various third party sites | Both |
| performance | Adds a faster JSON parser (ujson) and an ETF encoding parser | 2.x Only |
| sharding | Adds a library which is required to enable auto-sharding | 2.x Only |
| docs | Adds a library required to build this documentation | Both |
