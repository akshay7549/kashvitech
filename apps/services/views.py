from django.shortcuts import render
from datetime import datetime
from django.http import Http404


# ✅ COMMON SERVICES DATA (Reusable)
def get_services_data():
    return [
        {
            "title": "Web Development",
            "slug": "web-development",
            "icon": "fas fa-code",
            "description": "Modern, responsive and high-performance websites using Django, React & Bootstrap.",
            "color": "primary",
            "features": ["Responsive Design", "SEO Optimized", "Fast Loading"],
            "price": "₹9,999+",
            "badge": "🔥 Popular",
            "rating": 4.9,
            "category": "development",
            "is_featured": True,
        },
        {
            "title": "App Development",
            "slug": "app-development",
            "icon": "fas fa-mobile-alt",
            "description": "Android & iOS apps with smooth UI/UX and scalable backend systems.",
            "color": "success",
            "features": ["Flutter Apps", "API Integration", "User-Friendly UI"],
            "price": "₹19,999+",
            "badge": "📱 Trending",
            "rating": 4.8,
            "category": "development",
            "is_featured": True,
        },
        {
            "title": "Cloud Solutions",
            "slug": "cloud-solutions",
            "icon": "fas fa-cloud",
            "description": "Deploy and scale applications using AWS, Azure & Google Cloud.",
            "color": "info",
            "features": ["AWS Setup", "Cloud Hosting", "Scalability"],
            "price": "₹4,999+",
            "badge": "☁️ Scalable",
            "rating": 4.7,
            "category": "cloud",
            "is_featured": False,
        },
        {
            "title": "Cyber Security",
            "slug": "cyber-security",
            "icon": "fas fa-shield-alt",
            "description": "Protect systems with penetration testing and security monitoring.",
            "color": "danger",
            "features": ["Pen Testing", "Vulnerability Scan", "Security Audit"],
            "price": "₹14,999+",
            "badge": "🔐 Secure",
            "rating": 4.9,
            "category": "security",
            "is_featured": True,
        },
        {
            "title": "SEO & Marketing",
            "slug": "seo-marketing",
            "icon": "fas fa-chart-line",
            "description": "Grow your business with SEO, social media marketing and lead generation.",
            "color": "warning",
            "features": ["Google Ranking", "Ads Campaign", "Lead Generation"],
            "price": "₹7,999+",
            "badge": "📈 Growth",
            "rating": 4.6,
            "category": "marketing",
            "is_featured": False,
        },
        {
            "title": "Custom Software",
            "slug": "custom-software",
            "icon": "fas fa-cogs",
            "description": "Tailor-made software solutions for your business needs.",
            "color": "secondary",
            "features": ["ERP Systems", "Automation", "Custom Dashboard"],
            "price": "Custom",
            "badge": "⚙️ Custom",
            "rating": 4.8,
            "category": "software",
            "is_featured": False,
        },

        # ✅ NEW SERVICES
        {
            "title": "UI/UX Design",
            "slug": "ui-ux-design",
            "icon": "fas fa-pencil-ruler",
            "description": "Design modern, user-friendly and attractive interfaces.",
            "color": "pink",
            "features": ["Wireframes", "Figma Design", "User Experience"],
            "price": "₹5,999+",
            "badge": "🎨 Creative",
            "rating": 4.7,
            "category": "design",
            "is_featured": False,
        },
        {
            "title": "E-Commerce Development",
            "slug": "ecommerce",
            "icon": "fas fa-shopping-cart",
            "description": "Complete online store with payment gateway & admin panel.",
            "color": "dark",
            "features": ["Payment Gateway", "Admin Panel", "Order Tracking"],
            "price": "₹15,999+",
            "badge": "🛒 Business",
            "rating": 4.8,
            "category": "business",
            "is_featured": True,
        },
        {
            "title": "API Development",
            "slug": "api-development",
            "icon": "fas fa-plug",
            "description": "Secure and scalable REST APIs for apps and integrations.",
            "color": "info",
            "features": ["REST API", "JWT Auth", "Integration"],
            "price": "₹6,999+",
            "badge": "🔗 Integration",
            "rating": 4.6,
            "category": "development",
            "is_featured": False,
        },
        {
            "title": "DevOps Services",
            "slug": "devops",
            "icon": "fas fa-server",
            "description": "CI/CD pipelines, automation & cloud deployment.",
            "color": "secondary",
            "features": ["CI/CD", "Docker", "Automation"],
            "price": "₹8,999+",
            "badge": "⚡ Fast",
            "rating": 4.7,
            "category": "cloud",
            "is_featured": False,
        },
        {
            "title": "AI & Automation",
            "slug": "ai-automation",
            "icon": "fas fa-robot",
            "description": "AI chatbots, automation tools and smart systems.",
            "color": "primary",
            "features": ["Chatbots", "Automation", "AI Tools"],
            "price": "₹12,999+",
            "badge": "🤖 Smart",
            "rating": 4.9,
            "category": "ai",
            "is_featured": True,
        },
        {
            "title": "Maintenance & Support",
            "slug": "support",
            "icon": "fas fa-tools",
            "description": "24/7 maintenance, updates and bug fixing.",
            "color": "success",
            "features": ["Bug Fixes", "Updates", "24/7 Support"],
            "price": "₹2,999/mo",
            "badge": "🛠️ Support",
            "rating": 4.8,
            "category": "support",
            "is_featured": False,
        },
    ]


# ✅ SERVICES LIST VIEW (with search + filter)
def services_view(request):
    services = get_services_data()

    search_query = request.GET.get('q')
    category = request.GET.get('category')

    if search_query:
        services = [
            s for s in services
            if search_query.lower() in s['title'].lower()
        ]

    if category:
        services = [
            s for s in services
            if s['category'] == category
        ]

    highlight_service = next((s for s in services if s["is_featured"]), services[0])

    context = {
        "page_title": "Our Services | Kashvi Tech 🚀",
        "services": services,
        "total_services": len(services),
        "year": datetime.now().year,
        "highlight_service": highlight_service,
        "search_query": search_query,
        "selected_category": category,
    }

    return render(request, 'services/services.html', context)


# ✅ SERVICE DETAIL PAGE
def service_detail(request, slug):
    services = get_services_data()

    service = next((s for s in services if s["slug"] == slug), None)

    if not service:
        raise Http404("Service not found")

    return render(request, 'services/service_detail.html', {
        "service": service
    })