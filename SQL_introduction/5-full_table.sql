--
 SELECT
        TABLE_NAME,
        ENGINE,
        VERSION,
        ROW_FORMAT,
        TABLE_ROWS,
        AVG_ROW_LENGTH,
        DATA_LENGTH,
        INDEX_LENGTH,
        CREATE_TIME,
        UPDATE_TIME
    FROM
        INFORMATION_SCHEMA.TABLES
    WHERE
        TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';

