def invalidate_following_cache(sender, instance, **kwargs):
    # 为防止循环引用，把这个import写在函数内
    from friendships.services import FriendshipService
    FriendshipService.invalidate_following_cache(instance.from_user_id)