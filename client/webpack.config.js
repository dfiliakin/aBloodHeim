const webpack = require('webpack');
const dotenv = require('dotenv');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

// Load variables from the .env file
const env = dotenv.config().parsed || {};

module.exports = {
    mode: 'development', // or 'production'
    entry: './src/index.tsx',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.js', '.jsx'],
    },
    module: {
        rules: [
            {
                test: /\.(ts|tsx)$/,
                use: 'ts-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
        ],
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './public/index.html',
        }),

        new webpack.DefinePlugin({
            'process.env': JSON.stringify(env), // Inject all environment variables
        }),
    ],
    devServer: {
        static: path.join(__dirname, 'public'),
        port: 3000,
        server: {
            type: 'https',
            options: {
                key: path.join(__dirname, '../key.pem'),
                cert: path.join(__dirname, '../cert.pem'),
            },
        },
    },
};
