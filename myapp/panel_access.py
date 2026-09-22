"""Registry mapping panel URL names to permission sections, for the
sub-admin / teacher permission system.

Full admins (is_superuser=True, or is_staff with panel_access_all=True)
always have access to everything and are not affected by any of this.
"""

from django.shortcuts import render

PANEL_SECTIONS = [
    ('Overview', [
        ('signups', 'Signups'),
    ]),
    ('Customization', [
        ('customization_hero', 'Hero section'),
        ('customization_navbar', 'Navbar'),
        ('customization_banner', 'Banner'),
        ('customization_homepage', 'Homepage content'),
        ('customization_exam_ticker', 'Exam ticker'),
        ('customization_results', 'Results photos'),
        ('customization_footer', 'Footer'),
        ('customization_contact_page', 'Contact page'),
        ('customization_extra_pages', 'Extra pages (incl. FAQ)'),
    ]),
    ('Content', [
        ('categories', 'Categories & brands'),
        ('test_series', 'Test Series'),
        ('video_courses', 'Video Courses'),
        ('elibrary', 'E-Library'),
        ('bundles', 'Bundles'),
        ('classrooms', 'Classrooms'),
    ]),
    ('Commerce', [
        ('store_products', 'E-Store products'),
        ('store_orders', 'E-Store orders'),
        ('store_coupons', 'Coupons'),
        ('refer_earn', 'Refer & Earn'),
        ('career_jobs', 'Career: Post Job'),
        ('career_applications', 'Career: Applications'),
        ('razorpay', 'Razorpay'),
        ('sms_email', 'SMS & Email'),
        ('sso', 'SSO Login'),
        ('dropbox', 'Database Backup'),
    ]),
    ('Operations (ERP)', [
        ('erp_dashboard', 'ERP Dashboard'),
        ('erp_staff', 'Staff'),
        ('erp_attendance', 'Staff attendance'),
        ('erp_payroll', 'Payroll'),
        ('erp_student_attendance', 'Student attendance'),
        ('erp_fees', 'Fees'),
        ('erp_accounts', 'Accounts'),
    ]),
    ('Engagement', [
        ('notifications', 'Notifications'),
        ('chatbot', 'Chatbot'),
        ('daily_updates', 'Current Affairs'),
        ('gallery', 'Gallery'),
        ('quiz', 'Quiz Game'),
        ('certificates', 'Certificates'),
        ('exam_calendar', 'Exam Calendar'),
        ('eligibility', 'Eligibility'),
        ('admissions', 'Offline Admission'),
        ('contact_messages', 'Contact Messages'),
    ]),
    ('Settings', [
        ('pwa', 'Apps'),
    ]),
]

ALL_SECTION_KEYS = {key for _, items in PANEL_SECTIONS for key, _ in items}

# Views shared across multiple course types resolve their section from the
# `course_type` url kwarg instead of a fixed mapping below.
_COURSE_TYPE_SECTION = {
    'test_series': 'test_series',
    'video_course': 'video_courses',
    'elibrary': 'elibrary',
}
COURSE_TYPE_VIEW_URL_NAMES = {
    'panel_course_list', 'panel_course_add', 'panel_course_edit', 'panel_course_delete',
    'panel_course_content', 'panel_course_content_folder',
    'panel_course_content_folder_edit', 'panel_course_content_folder_delete',
    'panel_course_content_item_edit', 'panel_course_content_item_delete',
}

URL_SECTION_MAP = {
    # 'panel_dashboard' intentionally left unmapped: every admin user,
    # however restricted, can land on the dashboard.

    'panel_signups': 'signups',
    'panel_signup_add': 'signups',
    'panel_bulk_signup': 'signups',
    'panel_signup_edit': 'signups',
    'panel_signup_delete': 'signups',

    'panel_navbar_customization': 'customization_navbar',
    'panel_hero_section': 'customization_hero',
    'panel_banner_list': 'customization_banner',
    'panel_banner_add': 'customization_banner',
    'panel_banner_edit': 'customization_banner',
    'panel_banner_delete': 'customization_banner',

    'panel_notification_list': 'notifications',
    'panel_notification_add': 'notifications',
    'panel_notification_edit': 'notifications',
    'panel_notification_delete': 'notifications',
    'panel_notification_image_add': 'notifications',
    'panel_notification_image_delete': 'notifications',
    'panel_notification_link_add': 'notifications',
    'panel_notification_link_delete': 'notifications',
    'panel_notification_table_add': 'notifications',
    'panel_notification_table_delete': 'notifications',
    'panel_notification_table_row_add': 'notifications',
    'panel_notification_table_row_delete': 'notifications',
    'panel_notification_table_row_add_legacy': 'notifications',
    'panel_notification_table_row_delete_legacy': 'notifications',

    'panel_chatbot_list': 'chatbot',
    'panel_chatbot_question_add': 'chatbot',
    'panel_chatbot_question_edit': 'chatbot',
    'panel_chatbot_question_delete': 'chatbot',

    'panel_daily_updates': 'daily_updates',
    'panel_daily_post_add': 'daily_updates',
    'panel_daily_post_edit': 'daily_updates',
    'panel_daily_post_delete': 'daily_updates',
    'panel_daily_post_table_add': 'daily_updates',
    'panel_daily_post_table_delete': 'daily_updates',
    'panel_daily_post_table_row_add': 'daily_updates',
    'panel_daily_post_table_row_delete': 'daily_updates',
    'panel_daily_post_table_row_add_legacy': 'daily_updates',
    'panel_daily_post_table_row_delete_legacy': 'daily_updates',

    'panel_admissions': 'admissions',
    'panel_admission_delete': 'admissions',

    'panel_contact_messages': 'contact_messages',
    'panel_contact_message_delete': 'contact_messages',

    'panel_pwa_settings': 'pwa',

    'panel_gallery_list': 'gallery',
    'panel_gallery_add': 'gallery',
    'panel_gallery_edit': 'gallery',
    'panel_gallery_delete': 'gallery',

    'panel_brand_list': 'categories',
    'panel_brand_add': 'categories',
    'panel_brand_edit': 'categories',
    'panel_brand_delete': 'categories',
    'panel_category_list': 'categories',
    'panel_category_add': 'categories',
    'panel_category_edit': 'categories',
    'panel_category_delete': 'categories',

    'panel_test_series_customization': 'test_series',
    'panel_test_series_categories': 'test_series',
    'panel_test_series_category_add': 'test_series',
    'panel_test_series_category_edit': 'test_series',
    'panel_test_series_category_delete': 'test_series',
    'panel_question_list': 'test_series',
    'panel_question_add': 'test_series',
    'panel_question_bulk_upload': 'test_series',
    'panel_question_bulk_template': 'test_series',
    'panel_question_edit': 'test_series',
    'panel_question_delete': 'test_series',
    'panel_question_bulk_delete': 'test_series',
    'panel_question_detail': 'test_series',

    'panel_razorpay_settings': 'razorpay',
    'panel_notification_provider_settings': 'sms_email',
    'panel_sso_settings': 'sso',
    'panel_dropbox_settings': 'dropbox',

    'panel_store_product_list': 'store_products',
    'panel_store_product_add': 'store_products',
    'panel_store_product_edit': 'store_products',
    'panel_store_product_delete': 'store_products',
    'panel_store_orders': 'store_orders',
    'panel_store_order_update': 'store_orders',

    'panel_career_job_list': 'career_jobs',
    'panel_career_job_add': 'career_jobs',
    'panel_career_job_edit': 'career_jobs',
    'panel_career_job_delete': 'career_jobs',
    'panel_career_applications': 'career_applications',
    'panel_career_application_delete': 'career_applications',

    'panel_footer_settings': 'customization_footer',
    'panel_contact_page_settings': 'customization_contact_page',
    'panel_extra_page_list': 'customization_extra_pages',
    'panel_extra_page_edit': 'customization_extra_pages',
    'panel_faq_list': 'customization_extra_pages',
    'panel_faq_add': 'customization_extra_pages',
    'panel_faq_edit': 'customization_extra_pages',
    'panel_faq_delete': 'customization_extra_pages',

    'panel_exam_calendar_list': 'exam_calendar',
    'panel_exam_calendar_add': 'exam_calendar',
    'panel_exam_calendar_edit': 'exam_calendar',
    'panel_exam_calendar_delete': 'exam_calendar',

    'panel_homepage_content': 'customization_homepage',
    'panel_exam_ticker': 'customization_exam_ticker',
    'panel_result_list': 'customization_results',
    'panel_result_add': 'customization_results',
    'panel_result_edit': 'customization_results',
    'panel_result_delete': 'customization_results',

    'panel_bundle_list': 'bundles',
    'panel_bundle_add': 'bundles',
    'panel_bundle_edit': 'bundles',
    'panel_bundle_delete': 'bundles',

    'panel_classroom_list': 'classrooms',
    'panel_classroom_add': 'classrooms',
    'panel_classroom_edit': 'classrooms',
    'panel_classroom_delete': 'classrooms',
    'panel_classroom_students': 'classrooms',
    'panel_classroom_member_remove': 'classrooms',

    'panel_refer_earn': 'refer_earn',
    'panel_coupon_list': 'store_coupons',
    'panel_coupon_add': 'store_coupons',
    'panel_coupon_edit': 'store_coupons',
    'panel_coupon_delete': 'store_coupons',

    'panel_certificate_list': 'certificates',
    'panel_certificate_add': 'certificates',
    'panel_certificate_delete': 'certificates',

    'panel_quiz_question_list': 'quiz',
    'panel_quiz_music_update': 'quiz',
    'panel_quiz_question_add': 'quiz',
    'panel_quiz_question_edit': 'quiz',
    'panel_quiz_question_delete': 'quiz',

    'panel_eligibility_criteria_list': 'eligibility',
    'panel_eligibility_criteria_add': 'eligibility',
    'panel_eligibility_criteria_edit': 'eligibility',
    'panel_eligibility_criteria_delete': 'eligibility',
    'panel_eligibility_submissions': 'eligibility',

    'panel_erp_dashboard': 'erp_dashboard',
    'panel_staff_list': 'erp_staff',
    'panel_staff_add': 'erp_staff',
    'panel_staff_edit': 'erp_staff',
    'panel_staff_delete': 'erp_staff',
    'panel_attendance': 'erp_attendance',
    'panel_payroll_list': 'erp_payroll',
    'panel_payroll_generate': 'erp_payroll',
    'panel_payroll_edit': 'erp_payroll',
    'panel_payroll_mark_paid': 'erp_payroll',
    'panel_payroll_delete': 'erp_payroll',
    'panel_student_attendance': 'erp_student_attendance',
    'panel_fee_list': 'erp_fees',
    'panel_fee_add': 'erp_fees',
    'panel_fee_edit': 'erp_fees',
    'panel_fee_delete': 'erp_fees',
    'panel_fee_mark_paid': 'erp_fees',
    'panel_student_fee_ledger': 'erp_fees',
    'panel_account_list': 'erp_accounts',
    'panel_account_add': 'erp_accounts',
    'panel_account_delete': 'erp_accounts',
}

# URL names that are only ever reachable by full admins (managing other
# admin users' access). Not part of the checkbox grid on purpose.
ADMIN_ONLY_URL_NAMES = {
    'panel_admin_user_list',
    'panel_admin_user_add',
    'panel_admin_user_permissions',
    'panel_admin_user_remove',
}


def resolve_section_key(url_name, view_kwargs):
    if url_name in COURSE_TYPE_VIEW_URL_NAMES:
        course_type = (view_kwargs or {}).get('course_type', '')
        return _COURSE_TYPE_SECTION.get(course_type)
    return URL_SECTION_MAP.get(url_name)


def user_is_full_admin(user):
    return bool(user.is_authenticated and user.is_staff and (user.is_superuser or user.panel_access_all))


def user_allowed_sections(user):
    """Set of section keys this user may access. Full admins get everything."""
    if not user.is_authenticated or not user.is_staff:
        return set()
    if user_is_full_admin(user):
        return set(ALL_SECTION_KEYS)
    return set(user.panel_permissions or [])


def user_can_access_section(user, section_key):
    if not section_key:
        return True
    if not user.is_authenticated or not user.is_staff:
        return False
    if user_is_full_admin(user):
        return True
    return section_key in (user.panel_permissions or [])


class PanelAccessMiddleware:
    """Blocks staff users with restricted panel access from URLs whose
    section isn't in their allowed list. Superusers / full admins pass
    through untouched; non-staff users are handled by the existing
    @user_passes_test(_is_staff) decorators on each view.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        user = getattr(request, 'user', None)
        if user is None or not user.is_authenticated or not user.is_staff:
            return None
        if user_is_full_admin(user):
            return None

        match = request.resolver_match
        url_name = match.url_name if match else None
        if url_name is None:
            return None

        if url_name in ADMIN_ONLY_URL_NAMES:
            return render(request, 'myapp/panel/no_access.html', status=403)

        section_key = resolve_section_key(url_name, view_kwargs)
        if section_key and section_key not in (user.panel_permissions or []):
            return render(request, 'myapp/panel/no_access.html', status=403)
        return None


def panel_permissions_context(request):
    """Template context processor: exposes the current user's panel
    access so nav links can hide sections they can't reach.
    """
    user = getattr(request, 'user', None)
    if user is None or not user.is_authenticated:
        return {}
    return {
        'panel_is_full_admin': user_is_full_admin(user) if user.is_staff else False,
        'panel_allowed_sections': user_allowed_sections(user),
    }
