### BRAVE TESTING

[Web API provider](https://reqres.in/)
#### Requires
- Git
- Python3
- Curl or Wget


#### Project setup
**via curl**

```shell
curl -fsSL https://raw.githubusercontent.com/mosesokemwa/super-duper-octo-testing/master/setup | bash
```

**via wget**
```shell
wget -fsSL https://raw.githubusercontent.com/mosesokemwa/super-duper-octo-testing/master/setup | bash
```

#### Test cases not included
- There are no protected pages on the chosesn test api, so I cuold not test if the token works
- The page does not prevent double registration of user
- Does not provide redirect for failed authentication
- Does not provide error message for failed authorization
- No expiry of access tokens and renewal api route provided
