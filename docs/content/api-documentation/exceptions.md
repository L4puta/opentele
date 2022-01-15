<!-- vim: syntax=Markdown -->

# Exceptions

## Table of Contents

* [FileNotFound](#exception.FileNotFound)
* [TDataInvalidMagic](#exception.TDataInvalidMagic)
* [TDataInvalidCheckSum](#exception.TDataInvalidCheckSum)
* [TDataBadDecryptKey](#exception.TDataBadDecryptKey)
* [TDataWrongPasscode](#exception.TDataWrongPasscode)
* [TDataBadEncryptedDataSize](#exception.TDataBadEncryptedDataSize)
* [TDataBadDecryptedDataSize](#exception.TDataBadDecryptedDataSize)
* [TDataBadConfigData](#exception.TDataBadConfigData)
* [QDataStreamFailed](#exception.QDataStreamFailed)
* [AccountAuthKeyNotFound](#exception.AccountAuthKeyNotFound)
* [TDataReadMapDataFailed](#exception.TDataReadMapDataFailed)
* [TDataReadMapDataIncorrectPasscode](#exception.TDataReadMapDataIncorrectPasscode)
* [TDataAuthKeyNotFound](#exception.TDataAuthKeyNotFound)
* [MaxAccountLimit](#exception.MaxAccountLimit)
* [TDesktopUnauthorized](#exception.TDesktopUnauthorized)
* [TelethonUnauthorized](#exception.TelethonUnauthorized)
* [TDataSaveFailed](#exception.TDataSaveFailed)
* [TDesktopNotLoaded](#exception.TDesktopNotLoaded)
* [TDesktopHasNoAccount](#exception.TDesktopHasNoAccount)
* [TDAccountNotLoaded](#exception.TDAccountNotLoaded)
* [NoPasswordProvided](#exception.NoPasswordProvided)
* [Passwordincorrect](#exception.Passwordincorrect)
* [LoginFlagInvalid](#exception.LoginFlagInvalid)
* [NoInstanceMatched](#exception.NoInstanceMatched)
* [Expects](#exception.Expects)
* [Expects](#exception.Expects)

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L1)

<a id="exception.FileNotFound"></a>

## FileNotFound Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L60)

```python
class FileNotFound(OpenTeleException)
```

Could not find or open the file

<a id="exception.TDataInvalidMagic"></a>

## TDataInvalidMagic Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L65)

```python
class TDataInvalidMagic(OpenTeleException)
```

TData file has an invalid magic data, which is the first 4 bytes of the file\n
This usually mean that the file is corrupted or not in the supported formats

<a id="exception.TDataInvalidCheckSum"></a>

## TDataInvalidCheckSum Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L71)

```python
class TDataInvalidCheckSum(OpenTeleException)
```

TData file has an invalid checksum\n
This usually mean that the file is corrupted or not in the supported formats

<a id="exception.TDataBadDecryptKey"></a>

## TDataBadDecryptKey Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L77)

```python
class TDataBadDecryptKey(OpenTeleException)
```

Could not decrypt the data with this key\n
This usually mean that the file is password-encrypted

<a id="exception.TDataWrongPasscode"></a>

## TDataWrongPasscode Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L83)

```python
class TDataWrongPasscode(OpenTeleException)
```

Wrong passcode to decrypt tdata folder\n

<a id="exception.TDataBadEncryptedDataSize"></a>

## TDataBadEncryptedDataSize Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L88)

```python
class TDataBadEncryptedDataSize(OpenTeleException)
```

The encrypted data size part of the file is corrupted

<a id="exception.TDataBadDecryptedDataSize"></a>

## TDataBadDecryptedDataSize Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L92)

```python
class TDataBadDecryptedDataSize(OpenTeleException)
```

The decrypted data size part of the file is corrupted

<a id="exception.TDataBadConfigData"></a>

## TDataBadConfigData Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L96)

```python
class TDataBadConfigData(OpenTeleException)
```

TData contains bad config data that couldn't be parsed

<a id="exception.QDataStreamFailed"></a>

## QDataStreamFailed Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L101)

```python
class QDataStreamFailed(OpenTeleException)
```

Could not stream data from QDataStream\n
Please check the QDataStream.status() for more information

<a id="exception.AccountAuthKeyNotFound"></a>

## AccountAuthKeyNotFound Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L107)

```python
class AccountAuthKeyNotFound(OpenTeleException)
```

Account.authKey is missing, something went wrong

<a id="exception.TDataReadMapDataFailed"></a>

## TDataReadMapDataFailed Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L112)

```python
class TDataReadMapDataFailed(OpenTeleException)
```

Could not read map data

<a id="exception.TDataReadMapDataIncorrectPasscode"></a>

## TDataReadMapDataIncorrectPasscode Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L116)

```python
class TDataReadMapDataIncorrectPasscode(OpenTeleException)
```

Could not read map data because of incorrect passcode

<a id="exception.TDataAuthKeyNotFound"></a>

## TDataAuthKeyNotFound Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L120)

```python
class TDataAuthKeyNotFound(OpenTeleException)
```

Could not find authKey in TData

<a id="exception.MaxAccountLimit"></a>

## MaxAccountLimit Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L124)

```python
class MaxAccountLimit(OpenTeleException)
```

Maxed out limit for accounts per tdesktop client

<a id="exception.TDesktopUnauthorized"></a>

## TDesktopUnauthorized Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L129)

```python
class TDesktopUnauthorized(OpenTeleException)
```

TDesktop client is unauthorized

<a id="exception.TelethonUnauthorized"></a>

## TelethonUnauthorized Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L134)

```python
class TelethonUnauthorized(OpenTeleException)
```

Telethon client is unauthorized

<a id="exception.TDataSaveFailed"></a>

## TDataSaveFailed Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L139)

```python
class TDataSaveFailed(OpenTeleException)
```

Could not save TDesktop to tdata folder

<a id="exception.TDesktopNotLoaded"></a>

## TDesktopNotLoaded Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L144)

```python
class TDesktopNotLoaded(OpenTeleException)
```

TDesktop instance has no account

<a id="exception.TDesktopHasNoAccount"></a>

## TDesktopHasNoAccount Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L148)

```python
class TDesktopHasNoAccount(OpenTeleException)
```

TDesktop instance has no account

<a id="exception.TDAccountNotLoaded"></a>

## TDAccountNotLoaded Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L153)

```python
class TDAccountNotLoaded(OpenTeleException)
```

TDesktop account hasn't been loaded yet

<a id="exception.NoPasswordProvided"></a>

## NoPasswordProvided Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L157)

```python
class NoPasswordProvided(OpenTeleException)
```

You can't live without a password bro

<a id="exception.Passwordincorrect"></a>

## Passwordincorrect Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L162)

```python
class Passwordincorrect(OpenTeleException)
```

incorrect passwrd

<a id="exception.LoginFlagInvalid"></a>

## LoginFlagInvalid Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L167)

```python
class LoginFlagInvalid(OpenTeleException)
```

Invalid login flag

<a id="exception.NoInstanceMatched"></a>

## NoInstanceMatched Objects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L172)

```python
class NoInstanceMatched(OpenTeleException)
```

Invalid login flag

<a id="exception.Expects"></a>

#### Expects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L178)

```python
@typing.overload
def Expects(condition: bool, exception: str = None, done: typing.Callable[[],None] = None, fail: typing.Callable[[OpenTeleException],None] = None, silent: bool = False, stack_index: int = 1) -> bool
```

Expect a condition to be true, raise an OpenTeleException exception if it's not.
### Arguments
    1. condition (bool):\n
        Condition that you're expecting

### Optional
    2. message (OpenTeleException, default=None):\n
        custom exception message

    3. done (`typing.Callable[[],None]`, default=None):\n
        lambda to execute when done without error

    4. fail (`typing.Callable[[OpenTeleException],None]`, default=None):\n
        lambda to execute when the condition is False, the lambda will be execute before raising the exception

    5. silent (bool, default=False):\n
        if True then it won't raise the exception, only execute fail() lambda

    6. `stack_index` (int, default=1):\n
        stack index to raise the exception with trace back to where it happens, intended for internal usage

#### Raises:

- `exception` - OpenTeleException


<a id="exception.Expects"></a>

#### Expects

[[source]](https://github.com/thedemons/opentele/blob/c9036f76e4d63f9d6977e997a75bc17909c78d5a/src\exception.py#L213)

```python
@typing.overload
def Expects(condition: bool, exception: OpenTeleException = None, done: typing.Callable[[],None] = None, fail: typing.Callable[[OpenTeleException],None] = None, silent: bool = False, stack_index: int = 1) -> bool
```

Expect a condition to be true, raise an OpenTeleException exception if it's not.
### Arguments
    1. condition (bool):\n
        Condition that you're expecting

### Optional
    2. exception (OpenTeleException, default=None):\n
        custom exception to raise if False

    3. done (`typing.Callable[[],None]`, default=None):\n
        lambda to execute when done without error

    4. fail (`typing.Callable[[OpenTeleException],None]`, default=None):\n
        lambda to execute when the condition is False, the lambda will be execute before raising the exception

    5. silent (bool, default=False):\n
        if True then it won't raise the exception, only execute fail() lambda

    6. `stack_index` (int, default=1):\n
        stack index to raise the exception with trace back to where it happens, intended for internal usage

#### Raises:

- `exception` - OpenTeleException

