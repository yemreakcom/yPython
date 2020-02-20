# 🏗️ Kod içi Yapılar

## 📅 Tablo Oluşturma

```python
transition_table = {
        # Current state of the modifier, per `modifier_states`.
        # |
        # |             Type of event that triggered this modifier update.
        # |             |
        # |             |         Type of key that triggered this modiier update.
        # |             |         |
        # |             |         |            Should we send a fake key press?
        # |             |         |            |
        # |             |         |     =>     |       Accept the event?
        # |             |         |            |       |
        # |             |         |            |       |      Next state.
        # v             v         v            v       v      v
        ('free',       KEY_UP,   'modifier'): (False, True,  'free'),
        ('free',       KEY_DOWN, 'modifier'): (False, False, 'pending'),
        ('pending',    KEY_UP,   'modifier'): (True,  True,  'free'),
        ('pending',    KEY_DOWN, 'modifier'): (False, True,  'allowed'),
        ('suppressed', KEY_UP,   'modifier'): (False, False, 'free'),
        ('suppressed', KEY_DOWN, 'modifier'): (False, False, 'suppressed'),
        ('allowed',    KEY_UP,   'modifier'): (False, True,  'free'),
        ('allowed',    KEY_DOWN, 'modifier'): (False, True,  'allowed'),

        ('free',       KEY_UP,   'hotkey'):   (False, None,  'free'),
        ('free',       KEY_DOWN, 'hotkey'):   (False, None,  'free'),
        ('pending',    KEY_UP,   'hotkey'):   (False, None,  'suppressed'),
        ('pending',    KEY_DOWN, 'hotkey'):   (False, None,  'suppressed'),
        ('suppressed', KEY_UP,   'hotkey'):   (False, None,  'suppressed'),
        ('suppressed', KEY_DOWN, 'hotkey'):   (False, None,  'suppressed'),
        ('allowed',    KEY_UP,   'hotkey'):   (False, None,  'allowed'),
        ('allowed',    KEY_DOWN, 'hotkey'):   (False, None,  'allowed'),

        ('free',       KEY_UP,   'other'):    (False, True,  'free'),
        ('free',       KEY_DOWN, 'other'):    (False, True,  'free'),
        ('pending',    KEY_UP,   'other'):    (True,  True,  'allowed'),
        ('pending',    KEY_DOWN, 'other'):    (True,  True,  'allowed'),
        # Necessary when hotkeys are removed after beign triggered, such as
        # TestKeyboard.test_add_hotkey_multistep_suppress_modifier.
        ('suppressed', KEY_UP,   'other'):    (False, False, 'allowed'),
        ('suppressed', KEY_DOWN, 'other'):    (True,  True,  'allowed'),
        ('allowed',    KEY_UP,   'other'):    (False, True,  'allowed'),
        ('allowed',    KEY_DOWN, 'other'):    (False, True,  'allowed'),
    }
```

