## Ce que j'ai fait pour améliorer l'accessibilité

-J'ai ajouté un lien d'évitement sur les 2 pages pour aider les utilisateurs qui naviguent au clavier.

-J'ai mis une balise "header" avec le rôle "banner" sur les 2 pages pour une meilleure structure.

## Sur la page index
-j'ai remplacé le "h3" par un "h1" pour respecter la hiérarchie des titres.

-J'ai ajouté des "alt" sur toutes les images, surtout la première image de la page index qui n'en avait pas.

-J'ai transformé le lien de réservation en vrai bouton sur la page index pour une meilleure accessibilité.

-J'ai changé la couleur du texte dans le bandeau avec "--color-bandeau-text: #000000;" pour qu'on puisse 
 mieux le lire.

-La citation de Molière était en h6, je l'ai passée en h2 pour une meilleure structure.

-Dans la partie "Quelques chiffres", j'ai mis "aria-hidden="true"" sur les icônes pour que les lecteurs 
 d'écran ne les lisent pas en double.

-J'ai modifié "--color-secondary-text: #bcbcbc;" en "#d0d0d0" pour un meilleur contraste.

La section Galerie était en h4, je l'ai passée en h2 pour garder une structure logique.

-J'ai mis des textes alternatifs comme "alt="Scène de fin de présentation"" sur les images de la galerie.
 La section "Esprit du spectacle" était en h6, je l'ai passée en h2 comme les autres sections.

-J'ai ajouté des rôles ARIA comme navigation, main, banner, region et contentinfo pour aider les 
 technologies d'assistance.

-J'ai utilisé "aria-labelledby" pour relier les titres à leurs sections.

-J'ai mis des "aria-label" sur les éléments qui n'ont pas de texte visible.

## Sur la page infos 

j'ai amélioré le formulaire avec des labels bien associés et des attributs required.

-J'ai rendu le bouton du formulaire plus clair avec un texte explicite.

-J'ai créé une classe "sr-only" pour cacher visuellement du texte tout en le gardant accessible aux lecteurs 
 d'écran.

-J'ai amélioré la visibilité du focus sur tous les éléments interactifs.

-J'ai ajouté "tabindex="0"" sur tous les éléments interactifs pour qu'on puisse y accéder au clavier.

-J'ai optimisé les couleurs pour éliminer les problèmes de contraste.

-J'ai corrigé la hiérarchie des titres dans les sections réseaux sociaux et storytelling qui n'était pas  
 cohérente.
