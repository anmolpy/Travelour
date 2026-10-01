"""Checkpoint isolation. principal must come from verified server-side authentication."""
import hashlib
import json
import uuid


def checkpoint_identity(principal: str, thread_id: str | None = None):
    if not isinstance(principal, str) or not principal.strip() or len(principal) > 256:
        raise ValueError("An authenticated user identity is required")
    thread_id = thread_id or uuid.uuid4().hex
    if not isinstance(thread_id, str) or len(thread_id) > 128 or not thread_id:
        raise ValueError("Invalid conversation identifier")
    key = hashlib.sha256(json.dumps([principal, thread_id]).encode()).hexdigest()
    return thread_id, key
