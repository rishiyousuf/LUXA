// ============================================
// MAIN JAVASCRIPT - LUXURY WATCHES ECOMMERCE
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

// Initialize all functionality
function initializeApp() {
    addScrollAnimations();
    setupMobileMenu();
    setupFormValidation();
    setupProductInteractions();
    setupCartInteractions();
}

// ============================================
// SCROLL ANIMATIONS
// ============================================

function addScrollAnimations() {
    // Observer for fade-in animations on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'fadeInUp 0.8s ease forwards';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    // Observe all product cards
    document.querySelectorAll('.product-card').forEach(card => {
        observer.observe(card);
    });

    // Observe trust items
    document.querySelectorAll('.trust-item').forEach(item => {
        observer.observe(item);
    });

    // Observe reason items
    document.querySelectorAll('.reason').forEach(reason => {
        observer.observe(reason);
    });
}

// ============================================
// MOBILE MENU
// ============================================

function setupMobileMenu() {
    const menuToggle = document.getElementById('menuToggle');
    if (!menuToggle) return;

    menuToggle.addEventListener('click', function() {
        const navMenu = document.querySelector('.nav-menu');
        navMenu.classList.toggle('active');
        
        // Simple animation
        if (navMenu.classList.contains('active')) {
            navMenu.style.display = 'flex';
            navMenu.style.flexDirection = 'column';
            navMenu.style.position = 'absolute';
            navMenu.style.top = '100%';
            navMenu.style.left = '0';
            navMenu.style.right = '0';
            navMenu.style.backgroundColor = 'var(--primary-color)';
            navMenu.style.zIndex = '99';
        } else {
            navMenu.style.display = 'flex';
        }
    });

    // Close menu when link is clicked
    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.addEventListener('click', function() {
            document.querySelector('.nav-menu').classList.remove('active');
        });
    });
}

// ============================================
// FORM VALIDATION
// ============================================

function setupFormValidation() {
    // Validate checkout form
    const checkoutForm = document.querySelector('.checkout-form');
    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function(e) {
            if (!validateCheckoutForm()) {
                e.preventDefault();
                showNotification('Please fill in all required fields', 'error');
            }
        });
    }

    // Validate auth form
    const authForm = document.querySelector('.auth-form');
    if (authForm) {
        authForm.addEventListener('submit', function(e) {
            if (!validateAuthForm()) {
                e.preventDefault();
            }
        });
    }

    // Validate contact form
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            if (!validateContactForm()) {
                e.preventDefault();
                showNotification('Please fill in all required fields', 'error');
            }
        });
    }
}

function validateCheckoutForm() {
    const firstName = document.querySelector('input[name="first_name"]');
    const email = document.querySelector('input[name="email"]');
    const phone = document.querySelector('input[name="phone"]');
    const address = document.querySelector('input[name="address"]');
    
    if (!firstName?.value || !email?.value || !phone?.value || !address?.value) {
        return false;
    }
    
    if (!isValidEmail(email.value)) {
        showNotification('Please enter a valid email address', 'error');
        return false;
    }
    
    return true;
}

function validateAuthForm() {
    const password = document.querySelector('input[name="password"]');
    const confirmPassword = document.querySelector('input[name="confirm_password"]');
    
    if (confirmPassword && password.value !== confirmPassword.value) {
        showNotification('Passwords do not match', 'error');
        return false;
    }
    
    if (password.value.length < 6) {
        showNotification('Password must be at least 6 characters', 'error');
        return false;
    }
    
    return true;
}

function validateContactForm() {
    const name = document.querySelector('input[name="name"]');
    const email = document.querySelector('input[name="email"]');
    const message = document.querySelector('textarea[name="message"]');
    
    return name?.value && email?.value && message?.value && isValidEmail(email.value);
}

function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// ============================================
// PRODUCT INTERACTIONS
// ============================================

function setupProductInteractions() {
    // Add hover effects to product cards
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Product image gallery
    setupImageGallery();

    // Add to cart quantity selector
    setupQuantitySelector();
}

function setupImageGallery() {
    const thumbnails = document.querySelectorAll('.thumbnail');
    if (thumbnails.length === 0) return;

    thumbnails.forEach(thumb => {
        thumb.addEventListener('click', function() {
            const mainImage = document.getElementById('mainImage');
            const newSrc = this.src;
            
            // Fade effect
            mainImage.style.opacity = '0.5';
            setTimeout(() => {
                mainImage.src = newSrc;
                mainImage.style.opacity = '1';
            }, 150);

            // Update active state
            thumbnails.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

function setupQuantitySelector() {
    const quantityInputs = document.querySelectorAll('input[name="quantity"]');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            if (this.value < 1) {
                this.value = 1;
            }
            if (this.value > 10) {
                this.value = 10;
            }
        });
    });
}

// ============================================
// CART INTERACTIONS
// ============================================

function setupCartInteractions() {
    // Quantity update in cart
    const quantityForms = document.querySelectorAll('.quantity-form');
    quantityForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const input = this.querySelector('input[name="quantity"]');
            if (input.value < 1) {
                e.preventDefault();
                input.value = 1;
            }
        });
    });

    // Cart item animations
    document.querySelectorAll('.cart-item').forEach((item, index) => {
        item.style.animation = `fadeInUp 0.6s ease forwards`;
        item.style.animationDelay = `${index * 0.1}s`;
    });
}

// ============================================
// NOTIFICATIONS
// ============================================

function showNotification(message, type = 'info') {
    // Remove existing notifications
    document.querySelectorAll('.alert').forEach(alert => {
        if (alert.parentNode) {
            alert.parentNode.removeChild(alert);
        }
    });

    // Create new notification
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    alert.style.position = 'fixed';
    alert.style.top = '80px';
    alert.style.left = '50%';
    alert.style.transform = 'translateX(-50%)';
    alert.style.zIndex = '1000';
    alert.style.maxWidth = '500px';
    alert.style.animation = 'slideDown 0.3s ease';

    document.body.appendChild(alert);

    // Auto-remove after 5 seconds
    setTimeout(() => {
        alert.style.animation = 'slideDown 0.3s ease reverse';
        setTimeout(() => {
            if (alert.parentNode) {
                alert.parentNode.removeChild(alert);
            }
        }, 300);
    }, 5000);
}

// ============================================
// SMOOTH SCROLLING
// ============================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;

        e.preventDefault();
        const element = document.querySelector(href);
        if (element) {
            element.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ============================================
// PRICE FILTER
// ============================================

function setupPriceFilter() {
    const minPriceInput = document.querySelector('input[name="min_price"]');
    const maxPriceInput = document.querySelector('input[name="max_price"]');

    if (minPriceInput && maxPriceInput) {
        [minPriceInput, maxPriceInput].forEach(input => {
            input.addEventListener('change', function() {
                if (this.value < 0) {
                    this.value = 0;
                }
            });
        });
    }
}

setupPriceFilter();

// ============================================
// TAB SWITCHING
// ============================================

function switchTab(tabName) {
    // Hide all tabs
    const tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(tab => tab.classList.remove('active'));
    
    // Remove active class from buttons
    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    
    // Show selected tab
    const selectedTab = document.getElementById(tabName);
    if (selectedTab) {
        selectedTab.classList.add('active');
        
        // Add active class to clicked button
        buttons.forEach(btn => {
            if (btn.textContent.toLowerCase().includes(tabName.toLowerCase())) {
                btn.classList.add('active');
            }
        });
    }
}

// Make switchTab available globally
window.switchTab = switchTab;

// ============================================
// LAZY LOADING IMAGES
// ============================================

function setupLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.getAttribute('data-src');
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));
}

setupLazyLoading();

// ============================================
// UTILITY FUNCTIONS
// ============================================

// Format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

// Debounce function for search/filter
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// ============================================
// PAGE LOAD ANIMATION
// ============================================

window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});

// ============================================
// CONSOLE MESSAGE
// ============================================

console.log('%cLUXA - Luxury Watches', 'font-size: 20px; font-weight: bold; color: #d4af37;');
console.log('%cWelcome to our premium eCommerce platform', 'font-size: 12px; color: #999;');
