<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wpdb' );

/** MySQL database username */
define( 'DB_USER', 'wpuser' );

/** MySQL database password */
define( 'DB_PASSWORD', '123456' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );

/** Database Charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The Database Collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */

define('AUTH_KEY',         '=67&o.InO(`#Z Q}l&Xe+e<&,@p%S(mB!RYjPyu(|BgB90#1Fzf|BWJ+#4X-Riae');
define('SECURE_AUTH_KEY',  '(Shkl[SMfw}L$_p)IWhNgE.7iw;jzd9[B>RXB:9?IKG^nHf+A@]X-#/)-PlcjYTQ');
define('LOGGED_IN_KEY',    'z[>-VWEuVaFld/t9fU17.X1yMLP1W zXf&+yRoRcx//=4=G@lCrj4r0+Fkpgt;oG');
define('NONCE_KEY',        '&Rlo=:~B%,VrAZJ|#s}n?hm=(,]}?C7UlHD(-_1K]3l0z/yyAR<7R}55}=!yZ]j1');
define('AUTH_SALT',        '6,MVt&tG.:Lw:-Gv#8c_mEHH*}8|2QF%Bj;}k7?<4hR[1Q?`U&qhr}GEeRIs@:E>');
define('SECURE_AUTH_SALT', 'd+-E=_u0KOPI,r^%r_J?|WyttI6m],36`1l+y@@75h.4zzXeawT7!0{mt~&g]#37');
define('LOGGED_IN_SALT',   'M~#C+0yZmOw)BLBB*9=&q`AN9E3X/a1Ey(,VvJGBViC,Yp!5/S@{YO)U7NP(f-KH');
define('NONCE_SALT',       ';{6uy?M@4]@9~B;pIR-4LR.k6JR:W9[Rm^n9Uw(+5pPA$e B&J#f],NLQm `Y^((');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';


/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
