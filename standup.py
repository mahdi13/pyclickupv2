from clickupv2 import ClickupV2Client


class StandupApp:
    def get_activities_of(self, client: ClickupV2Client, team_id, list_id, view_id, users=None):
        users = users or []
        result = client._request(
            'post', f'/v2/activity',
            params={
                'team_id': team_id,
                'parent': {
                    'id': list_id,
                    'type': 6
                },
                'filters': {
                    'search': '',
                    'fields': ['added_to_subcategory', 'removed_from_subcategory', 'comment_assigned',
                               'comment_resolved', 'assignee', 'attachments', 'checklist_items_added',
                               'checklist_item_assignee', 'checklist_item_resolved', 'resolved_items', 'comment',
                               'content', 'custom_fields', 'dependency_of', 'depends_on', 'linked_task', 'due_date',
                               'email_comment', 'gh_commit', 'gl_commit', 'gl_issue', 'gl_merge_request',
                               'gh_pull_request', 'github_pull_request', 'bb_commit', 'bb_pr_created', 'bb_pr_updated',
                               'bb_pr_approved', 'bb_pr_unapproved', 'bb_pr_fulfilled', 'bb_pr_rejected', 'bb_issue',
                               'bb_issue_updated', 'gl_task_branch', 'gh_task_branch', 'section_moved', 'duplicate',
                               'name', 'new_subtask', 'priority', 'reaction', 'recurrence_set', 'recurrence_set_2.0',
                               'recur', 'recur_2.0', 'recurrence_removed', 'copy_task_recur', 'recurrence_missed',
                               'points', 'start_date', 'status', 'tag', 'tag_removed', 'task_creation',
                               'template_merged', 'time_estimate', 'time_spent', 'follower', 'zoom_meeting'],
                    'users': users, 'subtasks': True}, 'task_filters': {'search': '', 'op': 'AND', 'fields': []},
                'email_filter_flag': True
            }
        )
        return result
