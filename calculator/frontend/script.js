/**
 * Professional Calculator - JavaScript
 * ===================================
 * 
 * A professional calculator with iOS-style UI, API integration,
 * celebratory animations, and sound effects.
 */

class ProfessionalCalculator {
    constructor() {
        this.currentInput = '0';
        this.previousInput = '';
        this.operator = null;
        this.waitingForOperand = false;
        this.history = JSON.parse(localStorage.getItem('calculatorHistory')) || [];
        this.apiBaseUrl = 'http://localhost:8000';
        
        this.initializeElements();
        this.bindEvents();
        this.updateDisplay();
        this.loadHistory();
        this.checkApiStatus();
        // Clear any existing confetti on initialization
        this.clearConfetti();
    }

    initializeElements() {
        // Display elements
        this.displayExpression = document.getElementById('displayExpression');
        this.displayResult = document.getElementById('displayResult');
        
        // Status indicator
        this.statusIndicator = document.getElementById('statusIndicator');
        this.statusDot = this.statusIndicator.querySelector('.status-dot');
        this.statusText = this.statusIndicator.querySelector('.status-text');
        
        // History elements
        this.historyPanel = document.getElementById('historyPanel');
        this.historyList = document.getElementById('historyList');
        this.clearHistoryBtn = document.getElementById('clearHistory');
        
        // Audio elements
        this.successSound = document.getElementById('successSound');
        this.errorSound = document.getElementById('errorSound');
        
        // Loading overlay
        this.loadingOverlay = document.getElementById('loadingOverlay');
        
        // Toast container
        this.toastContainer = document.getElementById('toastContainer');
        
        // Confetti canvas
        this.confettiCanvas = document.getElementById('confettiCanvas');
        this.setupConfetti();
    }

    bindEvents() {
        // Button clicks
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('calc-btn')) {
                this.handleButtonClick(e.target);
            }
        });

        // Keyboard support
        document.addEventListener('keydown', (e) => {
            this.handleKeyboard(e);
        });

        // History clear
        this.clearHistoryBtn.addEventListener('click', () => {
            this.clearHistory();
        });

        // Prevent context menu on long press
        document.addEventListener('contextmenu', (e) => {
            e.preventDefault();
        });
    }

    handleButtonClick(button) {
        const action = button.dataset.action;
        const number = button.dataset.number;
        const operator = button.dataset.operator;

        // Add button press animation
        button.classList.add('active');
        setTimeout(() => button.classList.remove('active'), 150);

        if (number !== undefined) {
            this.inputNumber(number);
        } else if (operator !== undefined) {
            this.inputOperator(operator);
        } else if (action !== undefined) {
            this.inputAction(action);
        }
    }

    handleKeyboard(e) {
        e.preventDefault();
        
        const key = e.key;
        
        if (key >= '0' && key <= '9' || key === '.') {
            this.inputNumber(key);
        } else if (key === '+' || key === '-') {
            this.inputOperator(key === '+' ? 'add' : 'subtract');
        } else if (key === '*') {
            this.inputOperator('multiply');
        } else if (key === '/') {
            this.inputOperator('divide');
        } else if (key === 'Enter' || key === '=') {
            this.inputAction('equals');
        } else if (key === 'Escape' || key === 'c' || key === 'C') {
            this.inputAction('clear');
        } else if (key === 'Backspace') {
            this.inputAction('backspace');
        }
    }

    inputNumber(num) {
        if (this.waitingForOperand) {
            this.currentInput = num;
            this.waitingForOperand = false;
        } else {
            this.currentInput = this.currentInput === '0' ? num : this.currentInput + num;
        }
        this.updateDisplay();
        // Clear any existing confetti when starting new input
        this.clearConfetti();
    }

    inputOperator(nextOperator) {
        const inputValue = parseFloat(this.currentInput);

        if (this.previousInput === '') {
            this.previousInput = inputValue;
        } else if (this.operator) {
            const currentValue = this.previousInput || 0;
            const newValue = this.performCalculation();

            this.currentInput = String(newValue);
            this.previousInput = newValue;
        }

        this.waitingForOperand = true;
        this.operator = nextOperator;
        this.updateDisplay();
    }

    inputAction(action) {
        switch (action) {
            case 'clear':
                this.clear();
                break;
            case 'backspace':
                this.backspace();
                break;
            case 'percentage':
                this.percentage();
                break;
            case 'equals':
                this.calculate();
                break;
        }
    }

    clear() {
        this.currentInput = '0';
        this.previousInput = '';
        this.operator = null;
        this.waitingForOperand = false;
        this.updateDisplay();
        // Clear any existing confetti when clearing
        this.clearConfetti();
    }

    backspace() {
        if (this.currentInput.length > 1) {
            this.currentInput = this.currentInput.slice(0, -1);
        } else {
            this.currentInput = '0';
        }
        this.updateDisplay();
    }

    percentage() {
        this.currentInput = String(parseFloat(this.currentInput) / 100);
        this.updateDisplay();
    }

    async calculate() {
        if (this.operator && this.previousInput !== '') {
            this.showLoading(true);
            
            try {
                const result = await this.performApiCalculation(
                    parseFloat(this.previousInput),
                    parseFloat(this.currentInput),
                    this.operator
                );
                
                this.addToHistory(`${this.previousInput} ${this.getOperatorSymbol(this.operator)} ${this.currentInput}`, result);
                this.currentInput = String(result);
                this.previousInput = '';
                this.operator = null;
                this.waitingForOperand = true;
                
                this.updateDisplay();
                this.showSuccessAnimation();
                this.playSuccessSound();
                this.showToast('Calculation successful!', 'success');
                
            } catch (error) {
                console.error('Calculation error:', error);
                this.showErrorAnimation();
                this.playErrorSound();
                this.showToast('Calculation failed!', 'error');
            } finally {
                this.showLoading(false);
            }
        }
    }

    async performApiCalculation(a, b, operation) {
        const response = await fetch(`${this.apiBaseUrl}/calculate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                a: a,
                b: b,
                operation: operation
            })
        });

        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }

        const data = await response.json();
        return data.result;
    }

    getOperatorSymbol(operator) {
        const symbols = {
            'add': '+',
            'subtract': '−',
            'multiply': '×',
            'divide': '÷'
        };
        return symbols[operator] || operator;
    }

    updateDisplay() {
        this.displayResult.textContent = this.currentInput;
        
        if (this.operator && this.previousInput !== '') {
            this.displayExpression.textContent = `${this.previousInput} ${this.getOperatorSymbol(this.operator)}`;
        } else {
            this.displayExpression.textContent = '';
        }
    }

    addToHistory(expression, result) {
        const historyItem = {
            id: Date.now(),
            expression: expression,
            result: result,
            timestamp: new Date().toLocaleTimeString()
        };
        
        this.history.unshift(historyItem);
        
        // Keep only last 50 calculations
        if (this.history.length > 50) {
            this.history = this.history.slice(0, 50);
        }
        
        this.saveHistory();
        this.renderHistory();
    }

    renderHistory() {
        this.historyList.innerHTML = '';
        
        this.history.forEach(item => {
            const historyItem = document.createElement('div');
            historyItem.className = 'history-item';
            historyItem.innerHTML = `
                <div class="history-expression">${item.expression}</div>
                <div class="history-result">${item.result}</div>
            `;
            
            historyItem.addEventListener('click', () => {
                this.currentInput = String(item.result);
                this.updateDisplay();
            });
            
            this.historyList.appendChild(historyItem);
        });
    }

    clearHistory() {
        this.history = [];
        this.saveHistory();
        this.renderHistory();
        this.showToast('History cleared!', 'success');
    }

    saveHistory() {
        localStorage.setItem('calculatorHistory', JSON.stringify(this.history));
    }

    loadHistory() {
        this.renderHistory();
    }

    async checkApiStatus() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/health`);
            if (response.ok) {
                this.setStatus('connected', 'API Connected');
            } else {
                this.setStatus('error', 'API Error');
            }
        } catch (error) {
            this.setStatus('error', 'API Offline');
        }
    }

    setStatus(type, text) {
        this.statusDot.className = `status-dot ${type}`;
        this.statusText.textContent = text;
    }

    showLoading(show) {
        if (show) {
            this.loadingOverlay.classList.add('show');
            this.setStatus('loading', 'Calculating...');
        } else {
            this.loadingOverlay.classList.remove('show');
            this.setStatus('connected', 'Ready');
        }
    }

    showSuccessAnimation() {
        this.displayResult.classList.add('success-animation');
        setTimeout(() => {
            this.displayResult.classList.remove('success-animation');
        }, 300);
        
        this.triggerConfetti();
    }

    showErrorAnimation() {
        this.displayResult.classList.add('error-animation');
        setTimeout(() => {
            this.displayResult.classList.remove('error-animation');
        }, 500);
    }

    playSuccessSound() {
        if (this.successSound) {
            this.successSound.currentTime = 0;
            this.successSound.play().catch(e => console.log('Audio play failed:', e));
        }
    }

    playErrorSound() {
        if (this.errorSound) {
            this.errorSound.currentTime = 0;
            this.errorSound.play().catch(e => console.log('Audio play failed:', e));
        }
    }

    showToast(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.textContent = message;
        
        this.toastContainer.appendChild(toast);
        
        setTimeout(() => toast.classList.add('show'), 100);
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }

    setupConfetti() {
        this.confettiCtx = this.confettiCanvas.getContext('2d');
        this.confettiCanvas.width = window.innerWidth;
        this.confettiCanvas.height = window.innerHeight;
        
        window.addEventListener('resize', () => {
            this.confettiCanvas.width = window.innerWidth;
            this.confettiCanvas.height = window.innerHeight;
        });
    }

    triggerConfetti() {
        // Clear any existing confetti first
        this.clearConfetti();
        
        const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57', '#ff9ff3'];
        const confettiCount = 150;
        
        for (let i = 0; i < confettiCount; i++) {
            this.createConfettiPiece(colors[Math.floor(Math.random() * colors.length)]);
        }
        
        // Auto-clear confetti after 3 seconds
        setTimeout(() => {
            this.clearConfetti();
        }, 3000);
    }

    createConfettiPiece(color) {
        const confetti = {
            x: Math.random() * this.confettiCanvas.width,
            y: -10,
            vx: (Math.random() - 0.5) * 4,
            vy: Math.random() * 3 + 2,
            color: color,
            size: Math.random() * 8 + 4,
            rotation: Math.random() * 360,
            rotationSpeed: (Math.random() - 0.5) * 20
        };
        
        this.animateConfetti(confetti);
    }

    animateConfetti(confetti) {
        const animate = () => {
            confetti.x += confetti.vx;
            confetti.y += confetti.vy;
            confetti.vy += 0.1; // gravity
            confetti.rotation += confetti.rotationSpeed;
            
            this.confettiCtx.save();
            this.confettiCtx.translate(confetti.x, confetti.y);
            this.confettiCtx.rotate(confetti.rotation * Math.PI / 180);
            this.confettiCtx.fillStyle = confetti.color;
            this.confettiCtx.fillRect(-confetti.size/2, -confetti.size/2, confetti.size, confetti.size);
            this.confettiCtx.restore();
            
            if (confetti.y < this.confettiCanvas.height + 10) {
                requestAnimationFrame(animate);
            } else {
                // Confetti has fallen off screen, clear it
                this.clearConfetti();
            }
        };
        
        animate();
    }

    clearConfetti() {
        // Clear the entire canvas
        if (this.confettiCtx) {
            this.confettiCtx.clearRect(0, 0, this.confettiCanvas.width, this.confettiCanvas.height);
        }
    }
}

// Initialize calculator when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ProfessionalCalculator();
});

// Service Worker registration for offline functionality
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}
