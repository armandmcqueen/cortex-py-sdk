# Changelog

## 0.1.0-alpha.5 (2025-08-02)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/armandmcqueen/cortex-py-sdk/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** api update ([a8fb2ae](https://github.com/armandmcqueen/cortex-py-sdk/commit/a8fb2aef06636793f72add24e4f3f4c12e0605b0))
* **api:** api update ([58ce8cb](https://github.com/armandmcqueen/cortex-py-sdk/commit/58ce8cb954ddb7b275b1050335d9662b39840de1))
* **api:** api update ([0e64666](https://github.com/armandmcqueen/cortex-py-sdk/commit/0e6466691fe3a186e4215fe5e920a7f46a81ffcc))
* **api:** api update ([457c403](https://github.com/armandmcqueen/cortex-py-sdk/commit/457c403fe09897c69b375507e26e1ff0335da1ab))
* **client:** add follow_redirects request option ([45bf3de](https://github.com/armandmcqueen/cortex-py-sdk/commit/45bf3de7da3b86083abcd5fd18248da0ead3718c))
* **client:** add support for aiohttp ([36bda66](https://github.com/armandmcqueen/cortex-py-sdk/commit/36bda66ad67ee6cceca73aa58b18801d88e7fea9))


### Bug Fixes

* **ci:** correct conditional ([0cb587f](https://github.com/armandmcqueen/cortex-py-sdk/commit/0cb587f16b09b7935cecd3e87073f335e973c4a0))
* **ci:** release-doctor — report correct token name ([82d899f](https://github.com/armandmcqueen/cortex-py-sdk/commit/82d899f60080c5f95f2c4a95ffdb035fcee46a95))
* **client:** correctly parse binary response | stream ([1fcd366](https://github.com/armandmcqueen/cortex-py-sdk/commit/1fcd36627de39fa6d8f77fa6a25c65a81e90d35e))
* **client:** don't send Content-Type header on GET requests ([aa2a094](https://github.com/armandmcqueen/cortex-py-sdk/commit/aa2a0947b4cd400675550d32104a575241e94462))
* **docs/api:** remove references to nonexistent types ([def6a66](https://github.com/armandmcqueen/cortex-py-sdk/commit/def6a6633188dfcb7bbc2e0b221530c937ed78c5))
* **parsing:** correctly handle nested discriminated unions ([9081bd6](https://github.com/armandmcqueen/cortex-py-sdk/commit/9081bd61e13f49beee2f90844c6139ff896fec44))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([e75e921](https://github.com/armandmcqueen/cortex-py-sdk/commit/e75e921cc4b9247152a3a3ef356ee9bd97beb0d4))


### Chores

* change publish docs url ([fbdc2ee](https://github.com/armandmcqueen/cortex-py-sdk/commit/fbdc2ee055f5871f75bb8f285ba3592e73cd25c1))
* **ci:** change upload type ([a54cef4](https://github.com/armandmcqueen/cortex-py-sdk/commit/a54cef460cd5491af1e04a660ef57bb7633a6c8e))
* **ci:** enable for pull requests ([b487f0b](https://github.com/armandmcqueen/cortex-py-sdk/commit/b487f0b782fcec9e6c03432c58ae8a64976b3987))
* **ci:** fix installation instructions ([3bced28](https://github.com/armandmcqueen/cortex-py-sdk/commit/3bced282de4b4b036e8717c6da8eb5f919304e7f))
* **ci:** only run for pushes and fork pull requests ([420d586](https://github.com/armandmcqueen/cortex-py-sdk/commit/420d586b357376d50659f393bda310cbd1fa47b6))
* **docs:** grammar improvements ([73b749c](https://github.com/armandmcqueen/cortex-py-sdk/commit/73b749ce84bc89281ec16d1b606335322a3e262f))
* **docs:** remove reference to rye shell ([2c6f669](https://github.com/armandmcqueen/cortex-py-sdk/commit/2c6f6694bd3bb8e731bc77fe40c9c7f75df1362e))
* **internal:** bump pinned h11 dep ([0837e93](https://github.com/armandmcqueen/cortex-py-sdk/commit/0837e93db31edb4c57ee1b33355382f84a49ec1d))
* **internal:** codegen related update ([65e22be](https://github.com/armandmcqueen/cortex-py-sdk/commit/65e22bed64c4f78858270b9228f7d7873f33b686))
* **internal:** codegen related update ([3e79149](https://github.com/armandmcqueen/cortex-py-sdk/commit/3e79149c2da1b701ea269aa857b4ad31daecce00))
* **internal:** update conftest.py ([f7678ac](https://github.com/armandmcqueen/cortex-py-sdk/commit/f7678ace2b18f2631526e63d1be33582df012d54))
* **package:** mark python 3.13 as supported ([bb230ed](https://github.com/armandmcqueen/cortex-py-sdk/commit/bb230ed7db092f74512f96c7deba4215c5691355))
* **readme:** fix version rendering on pypi ([c93837f](https://github.com/armandmcqueen/cortex-py-sdk/commit/c93837f8d159fcc38d50c8114f83acd66e99cbe3))
* **readme:** update badges ([5fb76bc](https://github.com/armandmcqueen/cortex-py-sdk/commit/5fb76bc4ba942020c444bde6044272214755efcf))
* **tests:** add tests for httpx client instantiation & proxies ([baef3e0](https://github.com/armandmcqueen/cortex-py-sdk/commit/baef3e09d3f0b571cc36be3b30caed5fa5d44b09))
* **tests:** run tests in parallel ([36fd92b](https://github.com/armandmcqueen/cortex-py-sdk/commit/36fd92ba309539843048814612f503f15d12cff5))
* **tests:** skip some failing tests on the latest python versions ([d6838a7](https://github.com/armandmcqueen/cortex-py-sdk/commit/d6838a7def7f258f1626f604da8988ba099b24f7))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([731e71b](https://github.com/armandmcqueen/cortex-py-sdk/commit/731e71b01d9646c0c58410236a2bb832e29ed552))

## 0.1.0-alpha.4 (2025-05-15)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/armandmcqueen/cortex-py-sdk/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Bug Fixes

* **package:** support direct resource imports ([e0bc3e7](https://github.com/armandmcqueen/cortex-py-sdk/commit/e0bc3e757955bb02a0ad65824731257a1aa7b9ee))
* **pydantic v1:** more robust ModelField.annotation check ([6387aff](https://github.com/armandmcqueen/cortex-py-sdk/commit/6387aff7292101ab43350c52942f1a75b94ff6cb))


### Chores

* broadly detect json family of content-type headers ([59a8c04](https://github.com/armandmcqueen/cortex-py-sdk/commit/59a8c04873246a078ef8cdbbd971e04f1c8a6285))
* **ci:** add timeout thresholds for CI jobs ([598da4f](https://github.com/armandmcqueen/cortex-py-sdk/commit/598da4f4ac366c01c266d2d8ff85f3244f07abb3))
* **ci:** only use depot for staging repos ([32e8072](https://github.com/armandmcqueen/cortex-py-sdk/commit/32e80727b9276fd4344813a6104005ef94e6dc61))
* **ci:** upload sdks to package manager ([36803a1](https://github.com/armandmcqueen/cortex-py-sdk/commit/36803a165e9bb5a8af318fa87306137cd148c849))
* **client:** minor internal fixes ([2b6e970](https://github.com/armandmcqueen/cortex-py-sdk/commit/2b6e970d9ba67817791130da0e87d5ab21c05476))
* **internal:** avoid errors for isinstance checks on proxies ([1f67d0a](https://github.com/armandmcqueen/cortex-py-sdk/commit/1f67d0ae38ef9ff0b0a14f2ff147aa3e357b75b8))
* **internal:** base client updates ([6a79710](https://github.com/armandmcqueen/cortex-py-sdk/commit/6a79710e7e8ff3257cbbafa56a9a44274e3cedef))
* **internal:** bump pyright version ([d9fed2b](https://github.com/armandmcqueen/cortex-py-sdk/commit/d9fed2bac7fab8add4533f04aac34f6cf5241681))
* **internal:** codegen related update ([0b3fd8c](https://github.com/armandmcqueen/cortex-py-sdk/commit/0b3fd8cf218de3f9898ab5027d172cbeb8bb4918))
* **internal:** fix list file params ([e5f44e9](https://github.com/armandmcqueen/cortex-py-sdk/commit/e5f44e905f440403db2a00528d354f3d8817a4fc))
* **internal:** import reformatting ([6c06c05](https://github.com/armandmcqueen/cortex-py-sdk/commit/6c06c05b738b172c227ffd9c0853875e64bdeb7d))
* **internal:** minor formatting changes ([95cf379](https://github.com/armandmcqueen/cortex-py-sdk/commit/95cf3796b1af747c692b7d7e0accf02ed6c4cc4c))
* **internal:** refactor retries to not use recursion ([da36653](https://github.com/armandmcqueen/cortex-py-sdk/commit/da36653247bf7268a22a7cc4fff771c657b8d0b5))
* **internal:** update models test ([f950fef](https://github.com/armandmcqueen/cortex-py-sdk/commit/f950fef051433cf11a2f272370c8440643852dc4))
* **internal:** update pyright settings ([a1c4151](https://github.com/armandmcqueen/cortex-py-sdk/commit/a1c4151c485a876448071169d792e9c66979eb8f))

## 0.1.0-alpha.3 (2025-04-13)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/armandmcqueen/cortex-py-sdk/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** api update ([27f8c25](https://github.com/armandmcqueen/cortex-py-sdk/commit/27f8c25154435f18316ee9d20f54da260a3e9159))

## 0.1.0-alpha.2 (2025-04-13)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/armandmcqueen/cortex-py-sdk/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** api update ([09d7190](https://github.com/armandmcqueen/cortex-py-sdk/commit/09d7190cb57acfc7ab7625bd9daa8cfc51b7ef03))

## 0.1.0-alpha.1 (2025-04-13)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/armandmcqueen/cortex-py-sdk/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** api update ([08adb0f](https://github.com/armandmcqueen/cortex-py-sdk/commit/08adb0fb7219cb4e44d829ff69001632d7651b76))
* **api:** update via SDK Studio ([6c5308d](https://github.com/armandmcqueen/cortex-py-sdk/commit/6c5308d9d94523eeb980f714125ec72a1a707ec8))
* **api:** update via SDK Studio ([9f3770c](https://github.com/armandmcqueen/cortex-py-sdk/commit/9f3770ca196efc48b747a2b85df6f3ce9c841d70))


### Chores

* go live ([842c1a7](https://github.com/armandmcqueen/cortex-py-sdk/commit/842c1a7c7ffd7f83ef30f9a73bd3a66aece7a991))
* go live ([34762d3](https://github.com/armandmcqueen/cortex-py-sdk/commit/34762d305bd97a3d50e6bb2c8781c8398567e60b))
* update SDK settings ([b45055e](https://github.com/armandmcqueen/cortex-py-sdk/commit/b45055e9c20caafffeef324d493e0b3ce01efc53))
