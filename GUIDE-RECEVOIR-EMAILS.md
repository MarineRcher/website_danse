# Recevoir les emails sans configuration SMTP

## 🎯 Solution la plus simple : Formspree (Gratuit)

Formspree gère tout le traitement des emails. Vous recevez juste les messages dans votre boîte mail.

### ✅ Avantages

- **Gratuit** jusqu'à 50 soumissions/mois
- **Aucune configuration SMTP** nécessaire
- **Aucun code backend** à écrire
- **Protection anti-spam** intégrée
- **Confirmation automatique** à l'expéditeur

---

## 📝 Installation en 3 minutes

### Étape 1 : Créer un compte Formspree

1. Allez sur : https://formspree.io/
2. Cliquez sur "Get Started"
3. Inscrivez-vous avec votre email : **christianemataix@gmail.com**
4. Confirmez votre email

### Étape 2 : Créer un formulaire

1. Dans le dashboard, cliquez sur "+ New Form"
2. Donnez un nom : "Contact christianemataixdanse.fr"
3. Copiez l'ID du formulaire (format : `xxxxxxxxxxx`)

### Étape 3 : Modifier votre template HTML

Remplacez dans `website/templates/website/pages/contact/page.html` :

```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST"></form>
```

Par :

```html
<form action="https://formspree.io/f/xxxxxxxxxxx" method="POST"></form>
```

(Remplacez `xxxxxxxxxxx` par votre vrai ID)
