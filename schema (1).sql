-- schema.sql
-- Creates the database and table used by the Stock Market Analytics Dashboard.
-- Run this once before running fetch_stock_data.py for the first time.

CREATE DATABASE IF NOT EXISTS stock_analytics;
USE stock_analytics;

CREATE TABLE IF NOT EXISTS stock_prices (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    ticker         VARCHAR(20)   NOT NULL,
    date           DATE          NOT NULL,
    open_price     DECIMAL(12,4),
    high_price     DECIMAL(12,4),
    low_price      DECIMAL(12,4),
    close_price    DECIMAL(12,4),
    volume         BIGINT,
    ma7            DECIMAL(12,4),
    daily_return   DECIMAL(10,4),

    -- Prevents duplicate rows for the same stock on the same date
    UNIQUE KEY unique_ticker_date (ticker, date)
);
