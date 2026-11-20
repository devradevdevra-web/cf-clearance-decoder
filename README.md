# Challenge String Decoder

A lightweight Python utility for decoding Base64-encoded strings protected by a 16-bit byte-swapping XOR transformation.

## Overview

This utility reproduces the JavaScript `a0` decoding algorithm used in challenge platform bundles.

It takes an encoded string, Base64-decodes it, and reverses the XOR transformation to recover the original string.

## Decoding Algorithm

The decoder uses a fixed 16-bit initial state (seed):

```python
state = 36883
```

Hexadecimal representation:

```text
0x9013
```

The state is byte-swapped before each XOR operation. If the decoded byte is `0xFF`, the decoder reads two additional bytes to reconstruct a 16-bit character.

## Encoded Values

### 1. aB

**Base64 input:**

```text
PPN3/j7zdPk883vxf/x2/nT1PuB/8Wf2fOJ+v3u/
```

**Decoded result:**

```text
/cdn-cgi/challenge-platform/h/
```

### 2. aC

**Base64 input:**

```text
PPpg9Dz/ffVg+HzkPPYr9HWkd6RyoHD0Jb8jviGgJqYnpCakIqAjoyOjIqgkqiKnKqUioySmIqgp83vyXPMq1V/kfNNM2FqhfMYh2T7+XNkqxn3FUqIqx3j/cKR1o1TSV9ND+zw=
```

**Decoded result:**

```text
/jsd/oneshot/f8df4d4a0cd6/0.20564454100303187:1795137618:chbOc9ELtoC_HI1oV2I-nOI9VnUA29Wkoc4f3GBDCPk/
```

## Run

Execute the Python script:

```bash
python decoder.py
```

The script prints both decoded strings.

## Notes

- The initial seed is fixed at `36883`.
- Both supplied values use the same decoding algorithm.
- Input strings must be valid Base64.
- The decoder reproduces the string transformation used by the JavaScript function `a0`.
