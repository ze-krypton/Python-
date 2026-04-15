<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
        <head>
            <title>Book Catalog</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    background-color: #f5f5f5;
                }
                h2 {
                    color: #333;
                    text-align: center;
                }
                table {
                    width: 80%;
                    margin: 20px auto;
                    border-collapse: collapse;
                    background-color: #fff;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }
                th {
                    background-color: #2c3e50;
                    color: #fff;
                    padding: 12px 15px;
                    text-align: left;
                }
                td {
                    padding: 10px 15px;
                    border-bottom: 1px solid #ddd;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
                tr:hover {
                    background-color: #eaf2f8;
                }
            </style>
        </head>
        <body>

            <h2>Book Catalog</h2>

            <table>
                <tr>
                    <th>S.No</th>
                    <th>Title</th>
                    <th>Author</th>
                    <th>Year</th>
                    <th>Price ($)</th>
                </tr>

                <xsl:for-each select="catalog/book">
                    <xsl:sort select="year" />
                    <tr>
                        <td><xsl:value-of select="position()" /></td>
                        <td><xsl:value-of select="title" /></td>
                        <td><xsl:value-of select="author" /></td>
                        <td><xsl:value-of select="year" /></td>
                        <td><xsl:value-of select="price" /></td>
                    </tr>
                </xsl:for-each>

            </table>

        </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
