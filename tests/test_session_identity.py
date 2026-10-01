import unittest
from session_identity import checkpoint_identity

class IdentityTests(unittest.TestCase):
    def test_same_conversation_is_scoped_to_authenticated_user(self):
        self.assertNotEqual(checkpoint_identity('alice', 'same')[1], checkpoint_identity('bob', 'same')[1])
        self.assertEqual(checkpoint_identity('alice', 'same'), checkpoint_identity('alice', 'same'))
    def test_identity_required(self):
        for user in ['', None, ' ']:
            with self.assertRaises(ValueError):
                checkpoint_identity(user, 'same')
    def test_new_conversations_unique(self):
        self.assertNotEqual(checkpoint_identity('alice')[0], checkpoint_identity('alice')[0])
